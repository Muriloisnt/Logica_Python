"""
Sistema de Controle de Estoque - pequena empresa
-------------------------------------------------
Interface: Tkinter
Persistência: arquivos JSON (sem banco de dados)

Arquivos gerados na mesma pasta do programa:
    produtos.json       -> cadastro de produtos
    movimentacoes.json  -> histórico de entradas e saídas
    relatorio_estoque.txt -> relatório simples (gerado sob demanda)

Como executar:
    python estoque.py
"""

import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
PASTA = os.path.dirname(os.path.abspath(__file__))
ARQ_PRODUTOS = os.path.join(PASTA, "produtos.json")
ARQ_MOVIMENTOS = os.path.join(PASTA, "movimentacoes.json")
ARQ_RELATORIO = os.path.join(PASTA, "relatorio_estoque.txt")
FORMATO_DATA = "%d/%m/%Y"


# ---------------------------------------------------------------------------
# Persistência (leitura e gravação de JSON)
# ---------------------------------------------------------------------------
def carregar_json(caminho):
    """Lê uma lista de um arquivo JSON.

    - Arquivo inexistente: cria um arquivo vazio e retorna [].
    - Arquivo corrompido ou com erro de leitura: guarda uma cópia
      (.corrompido) para não perder nada e retorna [].
    """
    try:
        with open(caminho, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
        if not isinstance(dados, list):
            raise ValueError("O arquivo não contém uma lista.")
        return dados
    except FileNotFoundError:
        salvar_json(caminho, [])
        return []
    except (json.JSONDecodeError, ValueError, OSError) as erro:
        try:
            os.replace(caminho, caminho + ".corrompido")
        except OSError:
            pass
        messagebox.showwarning(
            "Aviso",
            f"Não foi possível ler '{os.path.basename(caminho)}' ({erro}).\n"
            "Uma cópia foi guardada como .corrompido e o sistema "
            "começará com dados vazios.",
        )
        return []


def salvar_json(caminho, dados):
    """Grava a lista em JSON. Escreve em arquivo temporário e depois
    substitui o original, evitando perder dados se algo falhar no meio."""
    temporario = caminho + ".tmp"
    try:
        with open(temporario, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, ensure_ascii=False, indent=4)
        os.replace(temporario, caminho)
    except OSError as erro:
        messagebox.showerror("Erro", f"Falha ao gravar o arquivo: {erro}")


# ---------------------------------------------------------------------------
# Regras de negócio e validações
# ---------------------------------------------------------------------------
def validar_inteiro(texto, campo, minimo=None):
    """Converte texto em inteiro, validando o valor mínimo."""
    try:
        valor = int(texto.strip())
    except ValueError:
        raise ValueError(f"{campo} deve ser um número inteiro.")
    if minimo is not None and valor < minimo:
        raise ValueError(f"{campo} deve ser maior ou igual a {minimo}.")
    return valor


def validar_produto(codigo, descricao, quantidade, minimo, preco):
    """Valida os campos do formulário e devolve o produto como dict."""
    descricao = descricao.strip()
    if not descricao:
        raise ValueError("O nome do produto é obrigatório.")

    codigo = validar_inteiro(codigo, "Código", 1)
    quantidade = validar_inteiro(quantidade, "Quantidade", 0)
    minimo = validar_inteiro(minimo, "Estoque mínimo", 0)

    try:
        preco = float(preco.strip().replace(",", "."))
    except ValueError:
        raise ValueError("Preço deve ser um número decimal.")
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

    return {
        "codigo": codigo,
        "descricao": descricao,
        "quantidade": quantidade,
        "estoque_minimo": minimo,
        "preco": round(preco, 2),
    }


def validar_data(texto):
    """Valida data no formato dd/mm/aaaa."""
    try:
        datetime.strptime(texto.strip(), FORMATO_DATA)
    except ValueError:
        raise ValueError("Data inválida. Use o formato dd/mm/aaaa.")
    return texto.strip()


class Estoque:
    """Guarda os produtos e movimentações e aplica as regras do sistema."""

    def __init__(self):
        self.produtos = carregar_json(ARQ_PRODUTOS)
        self.movimentos = carregar_json(ARQ_MOVIMENTOS)

    # --- utilitários -------------------------------------------------------
    def buscar_por_codigo(self, codigo):
        for produto in self.produtos:
            if produto["codigo"] == codigo:
                return produto
        return None

    def _gravar(self):
        salvar_json(ARQ_PRODUTOS, self.produtos)
        salvar_json(ARQ_MOVIMENTOS, self.movimentos)

    # --- cadastro ----------------------------------------------------------
    def incluir(self, produto):
        if self.buscar_por_codigo(produto["codigo"]):
            raise ValueError("Já existe um produto com este código.")
        self.produtos.append(produto)
        self.produtos.sort(key=lambda p: p["codigo"])
        self._gravar()

    def alterar(self, produto):
        existente = self.buscar_por_codigo(produto["codigo"])
        if not existente:
            raise ValueError("Produto não encontrado para alteração.")
        existente.update(produto)
        self._gravar()

    def excluir(self, codigo):
        existente = self.buscar_por_codigo(codigo)
        if not existente:
            raise ValueError("Produto não encontrado.")
        self.produtos.remove(existente)
        self._gravar()

    # --- movimentações -----------------------------------------------------
    def movimentar(self, tipo, codigo, quantidade, data):
        """Registra 'entrada' ou 'saida' e atualiza o estoque atual."""
        produto = self.buscar_por_codigo(codigo)
        if not produto:
            raise ValueError("Selecione um produto válido.")
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        if tipo == "entrada":
            produto["quantidade"] += quantidade      # estoque + entrada
        else:
            if quantidade > produto["quantidade"]:   # saída > estoque
                raise ValueError(
                    f"Estoque insuficiente. Disponível: {produto['quantidade']}."
                )
            produto["quantidade"] -= quantidade

        self.movimentos.append(
            {"codigo": codigo, "tipo": tipo, "quantidade": quantidade, "data": data}
        )
        self._gravar()

    # --- consultas ---------------------------------------------------------
    def consultar(self, modo, termo):
        termo = termo.strip()
        if not termo:
            return list(self.produtos)
        if modo == "codigo":
            codigo = validar_inteiro(termo, "Código")
            return [p for p in self.produtos if p["codigo"] == codigo]
        return [p for p in self.produtos if termo.lower() in p["descricao"].lower()]

    def estoque_baixo(self):
        return [p for p in self.produtos if p["quantidade"] <= p["estoque_minimo"]]

    def gerar_relatorio(self):
        """Gera um relatório de texto simples com o resumo do estoque."""
        total = sum(p["quantidade"] * p["preco"] for p in self.produtos)
        linhas = [
            "RELATÓRIO DE ESTOQUE",
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            "-" * 60,
            f"{'Cód':<6}{'Produto':<26}{'Qtd':>6}{'Mín':>6}{'Preço':>10}",
        ]
        for p in self.produtos:
            linhas.append(
                f"{p['codigo']:03d}   {p['descricao'][:24]:<26}"
                f"{p['quantidade']:>6}{p['estoque_minimo']:>6}{p['preco']:>10.2f}"
            )
        linhas += [
            "-" * 60,
            f"Total de produtos: {len(self.produtos)}",
            f"Produtos com estoque baixo: {len(self.estoque_baixo())}",
            f"Valor total em estoque: R$ {total:,.2f}",
        ]
        try:
            with open(ARQ_RELATORIO, "w", encoding="utf-8") as arq:
                arq.write("\n".join(linhas))
        except OSError as erro:
            raise ValueError(f"Não foi possível gerar o relatório: {erro}")
        return ARQ_RELATORIO


# ---------------------------------------------------------------------------
# Interface gráfica
# ---------------------------------------------------------------------------
def criar_tabela(pai, colunas):
    """Cria um Treeview com barra de rolagem. colunas = [(titulo, largura)]."""
    quadro = ttk.Frame(pai)
    tabela = ttk.Treeview(quadro, columns=[c[0] for c in colunas],
                          show="headings", height=10)
    for titulo, largura in colunas:
        tabela.heading(titulo, text=titulo)
        tabela.column(titulo, width=largura, anchor="center")
    barra = ttk.Scrollbar(quadro, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=barra.set)
    tabela.pack(side="left", fill="both", expand=True)
    barra.pack(side="right", fill="y")
    return quadro, tabela


class AbaProdutos(ttk.Frame):
    """Aba de cadastro: incluir, alterar, excluir e listar produtos."""

    def __init__(self, pai, app):
        super().__init__(pai, padding=10)
        self.app = app
        self.vars = {n: tk.StringVar() for n in
                     ("codigo", "descricao", "quantidade", "minimo", "preco")}

        form = ttk.LabelFrame(self, text="Dados do produto", padding=10)
        form.pack(fill="x")
        rotulos = [("Código", "codigo"), ("Nome", "descricao"),
                   ("Quantidade", "quantidade"), ("Estoque mínimo", "minimo"),
                   ("Preço unitário (R$)", "preco")]
        for i, (texto, chave) in enumerate(rotulos):
            ttk.Label(form, text=texto).grid(row=i // 2, column=(i % 2) * 2,
                                             sticky="e", padx=5, pady=4)
            ttk.Entry(form, textvariable=self.vars[chave], width=28).grid(
                row=i // 2, column=(i % 2) * 2 + 1, padx=5, pady=4)

        botoes = ttk.Frame(self)
        botoes.pack(fill="x", pady=8)
        for texto, comando in (("Incluir", self.incluir), ("Alterar", self.alterar),
                               ("Excluir", self.excluir), ("Limpar", self.limpar)):
            ttk.Button(botoes, text=texto, command=comando).pack(side="left", padx=4)

        quadro, self.tabela = criar_tabela(self, [
            ("Código", 70), ("Nome", 240), ("Quantidade", 90),
            ("Mínimo", 80), ("Preço", 90)])
        quadro.pack(fill="both", expand=True)
        self.tabela.bind("<<TreeviewSelect>>", self.selecionar)

    def _ler_formulario(self):
        v = self.vars
        return validar_produto(v["codigo"].get(), v["descricao"].get(),
                               v["quantidade"].get(), v["minimo"].get(),
                               v["preco"].get())

    def incluir(self):
        try:
            self.app.estoque.incluir(self._ler_formulario())
        except ValueError as erro:
            return messagebox.showerror("Erro", str(erro))
        messagebox.showinfo("Sucesso", "Produto cadastrado!")
        self.limpar()
        self.app.atualizar_tudo()

    def alterar(self):
        try:
            self.app.estoque.alterar(self._ler_formulario())
        except ValueError as erro:
            return messagebox.showerror("Erro", str(erro))
        messagebox.showinfo("Sucesso", "Produto alterado!")
        self.app.atualizar_tudo()

    def excluir(self):
        try:
            codigo = validar_inteiro(self.vars["codigo"].get(), "Código")
            if not self.app.estoque.buscar_por_codigo(codigo):
                raise ValueError("Selecione um produto existente na lista.")
            if not messagebox.askyesno("Confirmar", "Excluir este produto?"):
                return
            self.app.estoque.excluir(codigo)
        except ValueError as erro:
            return messagebox.showerror("Erro", str(erro))
        self.limpar()
        self.app.atualizar_tudo()

    def limpar(self):
        for var in self.vars.values():
            var.set("")
        self.tabela.selection_remove(self.tabela.selection())

    def selecionar(self, _evento=None):
        """Preenche o formulário com o produto selecionado na tabela."""
        item = self.tabela.selection()
        if not item:
            return
        codigo = int(self.tabela.item(item[0], "values")[0])
        p = self.app.estoque.buscar_por_codigo(codigo)
        if p:
            self.vars["codigo"].set(p["codigo"])
            self.vars["descricao"].set(p["descricao"])
            self.vars["quantidade"].set(p["quantidade"])
            self.vars["minimo"].set(p["estoque_minimo"])
            self.vars["preco"].set(f"{p['preco']:.2f}")

    def atualizar(self):
        self.tabela.delete(*self.tabela.get_children())
        for p in self.app.estoque.produtos:
            self.tabela.insert("", "end", values=(
                f"{p['codigo']:03d}", p["descricao"], p["quantidade"],
                p["estoque_minimo"], f"R$ {p['preco']:.2f}"))


class AbaMovimento(ttk.Frame):
    """Aba usada tanto para entrada quanto para saída de mercadorias."""

    def __init__(self, pai, app, tipo):
        super().__init__(pai, padding=15)
        self.app, self.tipo = app, tipo
        self.produto = tk.StringVar()
        self.quantidade = tk.StringVar()
        self.data = tk.StringVar(value=datetime.now().strftime(FORMATO_DATA))

        titulo = "Entrada de mercadorias" if tipo == "entrada" else "Saída de mercadorias"
        form = ttk.LabelFrame(self, text=titulo, padding=15)
        form.pack(anchor="n")
        ttk.Label(form, text="Produto").grid(row=0, column=0, sticky="e", pady=6)
        self.combo = ttk.Combobox(form, textvariable=self.produto,
                                  state="readonly", width=40)
        self.combo.grid(row=0, column=1, padx=6)
        ttk.Label(form, text="Quantidade").grid(row=1, column=0, sticky="e", pady=6)
        ttk.Entry(form, textvariable=self.quantidade, width=15).grid(
            row=1, column=1, sticky="w", padx=6)
        ttk.Label(form, text="Data (dd/mm/aaaa)").grid(row=2, column=0, sticky="e", pady=6)
        ttk.Entry(form, textvariable=self.data, width=15).grid(
            row=2, column=1, sticky="w", padx=6)
        ttk.Button(form, text="Registrar", command=self.registrar).grid(
            row=3, column=1, sticky="w", padx=6, pady=10)

    def registrar(self):
        try:
            if not self.produto.get():
                raise ValueError("Selecione um produto.")
            codigo = int(self.produto.get().split(" - ")[0])
            quantidade = validar_inteiro(self.quantidade.get(), "Quantidade", 1)
            data = validar_data(self.data.get())
            self.app.estoque.movimentar(self.tipo, codigo, quantidade, data)
        except ValueError as erro:
            return messagebox.showerror("Erro", str(erro))
        messagebox.showinfo("Sucesso", "Movimentação registrada!")
        self.quantidade.set("")
        self.app.atualizar_tudo()

    def atualizar(self):
        self.combo["values"] = [
            f"{p['codigo']} - {p['descricao']} (estoque: {p['quantidade']})"
            for p in self.app.estoque.produtos]
        self.produto.set("")


class AbaConsulta(ttk.Frame):
    """Aba de consulta de estoque por código ou por nome."""

    def __init__(self, pai, app):
        super().__init__(pai, padding=10)
        self.app = app
        self.modo = tk.StringVar(value="nome")
        self.termo = tk.StringVar()

        barra = ttk.Frame(self)
        barra.pack(fill="x", pady=(0, 8))
        ttk.Radiobutton(barra, text="Por nome", variable=self.modo,
                        value="nome").pack(side="left", padx=4)
        ttk.Radiobutton(barra, text="Por código", variable=self.modo,
                        value="codigo").pack(side="left", padx=4)
        entrada = ttk.Entry(barra, textvariable=self.termo, width=30)
        entrada.pack(side="left", padx=6)
        entrada.bind("<Return>", lambda _e: self.atualizar())
        ttk.Button(barra, text="Consultar", command=self.atualizar).pack(side="left")
        ttk.Button(barra, text="Mostrar todos", command=self.mostrar_todos).pack(
            side="left", padx=4)

        quadro, self.tabela = criar_tabela(self, [
            ("Código", 80), ("Produto", 300), ("Quantidade", 100)])
        quadro.pack(fill="both", expand=True)

    def mostrar_todos(self):
        self.termo.set("")
        self.atualizar()

    def atualizar(self):
        try:
            resultado = self.app.estoque.consultar(self.modo.get(), self.termo.get())
        except ValueError as erro:
            return messagebox.showerror("Erro", str(erro))
        self.tabela.delete(*self.tabela.get_children())
        for p in resultado:
            self.tabela.insert("", "end", values=(
                f"{p['codigo']:03d}", p["descricao"], p["quantidade"]))


class AbaEstoqueBaixo(ttk.Frame):
    """Aba com os produtos cuja quantidade é menor ou igual ao mínimo."""

    def __init__(self, pai, app):
        super().__init__(pai, padding=10)
        self.app = app
        ttk.Label(self, text="Produtos com quantidade <= estoque mínimo").pack(
            anchor="w", pady=(0, 6))
        quadro, self.tabela = criar_tabela(self, [
            ("Produto", 300), ("Quantidade", 100), ("Mínimo", 100)])
        quadro.pack(fill="both", expand=True)
        ttk.Button(self, text="Gerar relatório (.txt)",
                   command=self.gerar_relatorio).pack(anchor="e", pady=8)

    def gerar_relatorio(self):
        try:
            caminho = self.app.estoque.gerar_relatorio()
        except ValueError as erro:
            return messagebox.showerror("Erro", str(erro))
        messagebox.showinfo("Relatório", f"Relatório salvo em:\n{caminho}")

    def atualizar(self):
        self.tabela.delete(*self.tabela.get_children())
        for p in self.app.estoque.estoque_baixo():
            self.tabela.insert("", "end", values=(
                p["descricao"], p["quantidade"], p["estoque_minimo"]))


class App(tk.Tk):
    """Janela principal com as abas do sistema."""

    def __init__(self):
        super().__init__()
        self.title("Controle de Estoque")
        self.geometry("760x520")
        self.minsize(700, 480)
        self.estoque = Estoque()

        abas = ttk.Notebook(self)
        abas.pack(fill="both", expand=True, padx=8, pady=8)
        self.telas = [
            ("Produtos", AbaProdutos(abas, self)),
            ("Entrada", AbaMovimento(abas, self, "entrada")),
            ("Saída", AbaMovimento(abas, self, "saida")),
            ("Consulta", AbaConsulta(abas, self)),
            ("Estoque baixo", AbaEstoqueBaixo(abas, self)),
        ]
        for titulo, tela in self.telas:
            abas.add(tela, text=titulo)
        self.atualizar_tudo()

    def atualizar_tudo(self):
        """Recarrega todas as abas após qualquer alteração nos dados."""
        for _titulo, tela in self.telas:
            tela.atualizar()


if __name__ == "__main__":
    App().mainloop()