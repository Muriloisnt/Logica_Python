
import json
import os
from datetime import datetime

# nome do arquivo que armazena as movimentações
ARQUIVO = "movimentacoes.json"


# carrega as movimentações salvas no arquivo json
def carregar_movimentacoes():
    if not os.path.exists(ARQUIVO):
        # cria o arquivo caso ele ainda não exista
        salvar_movimentacoes([])
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

            # verifica se o conteúdo é uma lista ou não
            if isinstance(dados, list):
                return dados

            print("Erro: o arquivo JSON possui formato inválido.")
            return []

    except (json.JSONDecodeError, OSError):
        print("Erro ao ler o arquivo JSON. Iniciando lista vazia.")
        return []


# salva todas as movimentações no arquivo JSON
def salvar_movimentacoes(movimentacoes):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump(
                movimentacoes,
                arquivo,
                ensure_ascii=False,
                indent=4
            )
    except OSError:
        print("Erro: não foi possível salvar os dados.")


# formata os valores no padrão da moeda brasileira
def formatar_valor(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")
    return f"R$ {valor_formatado}"


# calcula o próximo identificador disponível
def gerar_id(movimentacoes):
    if not movimentacoes:
        return 1

    return max(mov["id"] for mov in movimentacoes) + 1


# cadastra uma receita ou uma despesa
def adicionar_movimentacao(movimentacoes, tipo):
    descricao = input("Descrição: ").strip()

    # impede o cadastro de descrições vazias
    if not descricao:
        print("Erro: a descrição não pode ficar vazia.")
        return

    # valida o valor informado pelo usuário
    try:
        entrada = input("Valor: ").strip()
        entrada = entrada.replace(",", ".")
        valor = float(entrada)

        if valor <= 0:
            print("Erro: o valor deve ser maior que zero.")
            return

    except ValueError:
        print("Erro: informe um valor numérico válido.")
        return

    # Registra automaticamente a data e a hora atuais
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

    # cria um dicionário para representar a movimentação
    movimentacao = {
        "id": gerar_id(movimentacoes),
        "descricao": descricao,
        "valor": round(valor, 2),
        "tipo": tipo,
        "data": data_hora
    }

    movimentacoes.append(movimentacao)

    # salva os dados imediatamente após a inclusão
    salvar_movimentacoes(movimentacoes)

    print(f"{tipo} cadastrada com sucesso!")
    print(f"Identificador: {movimentacao['id']}")
    print(f"Data e hora: {data_hora}")


# exibe todas as movimentações registradas
def listar_movimentacoes(movimentacoes):
    print("\n--- LISTA DE MOVIMENTAÇÕES ---")

    if not movimentacoes:
        print("Nenhuma movimentação cadastrada.")
        return

    for mov in movimentacoes:
        print(
            f"{mov['id']} - {mov['data']} | "
            f"{mov['tipo']} | "
            f"{formatar_valor(mov['valor'])} | "
            f"{mov['descricao']}"
        )


# Calcula e apresenta o saldo financeiro
def consultar_saldo(movimentacoes):
    total_receitas = sum(
        mov["valor"]
        for mov in movimentacoes
        if mov["tipo"] == "Receita"
    )

    total_despesas = sum(
        mov["valor"]
        for mov in movimentacoes
        if mov["tipo"] == "Despesa"
    )

    saldo = total_receitas - total_despesas

    print(f"\nSaldo atual: {formatar_valor(saldo)}")


# Exclui uma movimentação usando seu identificador
def excluir_movimentacao(movimentacoes):
    if not movimentacoes:
        print("Não existem movimentações para excluir.")
        return

    listar_movimentacoes(movimentacoes)

    try:
        identificador = int(
            input("\nInforme o ID da movimentação que deseja excluir: ")
        )
    except ValueError:
        print("Erro: informe um identificador numérico válido.")
        return

    for mov in movimentacoes:
        if mov["id"] == identificador:
            movimentacoes.remove(mov)
            salvar_movimentacoes(movimentacoes)
            print("Movimentação excluída com sucesso!")
            return

    print("Erro: não foi encontrada uma movimentação com esse ID.")


# gera o relatório financeiro completo
def gerar_relatorio(movimentacoes):
    total_receitas = sum(
        mov["valor"]
        for mov in movimentacoes
        if mov["tipo"] == "Receita"
    )

    total_despesas = sum(
        mov["valor"]
        for mov in movimentacoes
        if mov["tipo"] == "Despesa"
    )

    saldo = total_receitas - total_despesas
    quantidade = len(movimentacoes)

    print("\n--- RELATÓRIO FINANCEIRO ---")
    print(f"Total de Receitas: {formatar_valor(total_receitas)}")
    print(f"Total de Despesas: {formatar_valor(total_despesas)}")
    print(f"Saldo Atual: {formatar_valor(saldo)}")
    print(f"Quantidade de Movimentações: {quantidade}")


# apresenta o menu 
def exibir_menu():
    print("\n========== MENU ==========")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Listar Movimentações")
    print("4 - Consultar Saldo")
    print("5 - Excluir Movimentação")
    print("6 - Gerar Relatório")
    print("0 - Sair")
    print("==========================")


# função principal que controla a execução do programa
def main():
    movimentacoes = carregar_movimentacoes()

    print("Bem-vindo ao Controle de Gastos Pessoais!")

    # mantém o menu ativo até o usuário escolher sair
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_movimentacao(movimentacoes, "Receita")

        elif opcao == "2":
            adicionar_movimentacao(movimentacoes, "Despesa")

        elif opcao == "3":
            listar_movimentacoes(movimentacoes)

        elif opcao == "4":
            consultar_saldo(movimentacoes)

        elif opcao == "5":
            excluir_movimentacao(movimentacoes)

        elif opcao == "6":
            gerar_relatorio(movimentacoes)

        elif opcao == "0":
            print(
                "Obrigado por utilizar o Controle de Gastos Pessoais!"
            )
            break

        else:
            print("Opção inválida! Escolha uma opção disponível.")


# inicia o programa
if __name__ == "__main__":
    main()
