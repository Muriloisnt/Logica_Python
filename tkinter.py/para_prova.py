#1. Importa a biblioteca
#↓
#2. Cria a função
#↓
#3. Lê peso e altura
#↓
#4. Calcula o IMC
#↓
#5. Verifica a classificação
#↓
#6. Mostra o resultado
#↓
#7. Cria a janela
#↓
#8. Cria os textos
#↓
#9. Cria as caixas de entrada
#↓
#10. Cria o botão
#↓
#11. Mantém a janela aberta

# O QUE É O TKINTER?
# ============================================================

# O Tkinter é uma biblioteca do Python utilizada para criar
# interfaces gráficas (GUI - Graphical User Interface).
# Com ela é possível criar programas com janelas, botões,
# caixas de texto, menus, rótulos e outros componentes visuais.
#
# Sem o Tkinter, o programa funciona apenas no terminal.
# Com o Tkinter, o usuário pode interagir por meio de uma janela.

# ============================================================
# IMPORTANDO A BIBLIOTECA
# ============================================================

# import tkinter as tk
#
# Importa a biblioteca Tkinter para o programa.
# O "as tk" cria um apelido para facilitar a escrita do código.
#
# Em vez de escrever:
# tkinter.Label()
#
# Podemos escrever:
# tk.Label()

# ============================================================
# CRIANDO A JANELA
# ============================================================

# janela = tk.Tk()
#
# Cria a janela principal do programa.
# Todos os componentes da interface (botões, textos,
# caixas de entrada, etc.) serão adicionados dentro dessa janela.

# ============================================================
# TÍTULO DA JANELA
# ============================================================

# janela.title("Calculadora de IMC")
#
# Define o título que aparecerá na barra superior da janela.

# ============================================================
# TAMANHO DA JANELA
# ============================================================

# janela.geometry("250x250")
#
# Define o tamanho da janela.
# O primeiro número representa a largura e o segundo a altura,
# ambos em pixels.

# ============================================================
# LABEL (RÓTULO)
# ============================================================

# label = tk.Label(...)
#
# O Label cria um texto que será exibido na tela.
# Ele serve para orientar o usuário, mostrando informações
# como "Peso (kg):", "Altura (m):", "Resultado:", etc.

# ============================================================
# ENTRY (CAIXA DE ENTRADA)
# ============================================================

# entrada = tk.Entry(...)
#
# O Entry cria uma caixa onde o usuário pode digitar informações,
# como peso e altura.

# ============================================================
# GET()
# ============================================================

# entrada.get()
#
# O método get() lê o conteúdo digitado dentro do Entry.
# O valor retornado é uma string (texto).

# ============================================================
# BUTTON (BOTÃO)
# ============================================================

# botao = tk.Button(...)
#
# O Button cria um botão na janela.
# Quando o usuário clicar nele, uma função será executada.

# ============================================================
# COMMAND
# ============================================================

# command=calcular_imc
#
# O parâmetro command informa qual função será executada
# quando o botão for pressionado.
#
# Nesse caso, ao clicar no botão, a função calcular_imc()
# será chamada automaticamente.

# ============================================================
# PACK()
# ============================================================

# componente.pack()
#
# O método pack() posiciona o componente dentro da janela.
# Sem ele, o componente é criado, mas não aparece na tela.
#
# O parâmetro pady adiciona um espaço vertical entre
# os componentes da interface.

# ============================================================
# CONFIG()
# ============================================================

# label_resultado.config(...)
#
# O método config() altera as propriedades de um componente
# depois que ele já foi criado.
#
# No programa, ele é usado para atualizar o texto do resultado,
# mostrando o IMC e sua classificação.

# ============================================================
# FONT
# ============================================================

# font=("Arial", 10, "bold")
#
# Define a aparência do texto.
#
# "Arial" -> tipo da fonte.
# 10      -> tamanho da fonte.
# "bold"  -> deixa o texto em negrito.

# ============================================================
# MAINLOOP()
# ============================================================

# janela.mainloop()
#
# Inicia o laço principal da interface gráfica.
# Mantém a janela aberta e aguardando as ações do usuário,
# como digitar informações ou clicar em botões.
#
# Sem essa linha, a janela seria criada e fechada imediatamente.

# ============================================================
# RESUMO DO FUNCIONAMENTO DO TKINTER
# ============================================================

# 1. Importa a biblioteca Tkinter.
# 2. Cria a janela principal.
# 3. Define o título e o tamanho da janela.
# 4. Cria os componentes (Label, Entry e Button).
# 5. Posiciona os componentes usando pack().
# 6. Aguarda a interação do usuário através do mainloop().
# 7. Quando o botão é clicado, a função associada ao command é executada.