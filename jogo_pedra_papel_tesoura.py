import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

# pip install Pillow
from PIL import Image, ImageTk
# CORES
cor0 = '#FFFFFF'   # branco
cor1 = '#333333'   # preto / apagado
cor2 = '#fcc058'   # laranja
cor3 = '#fff873'   # amarelo
cor4 = '#34eb3d'   # verde
cor5 = '#e85151'   # vermelho
fundo = '#3b3b3b'

# JANELA

janela = Tk()

janela.title('Pedra, Papel e Tesoura')

janela.geometry('260x280')

janela.configure(bg=fundo)

janela.resizable(False, False)

# FRAMES

frame_cima = Frame(
    janela,
    width=260,
    height=110,
    bg=cor1,
    relief='raised'
)

frame_cima.grid(
    row=0,
    column=0,
    sticky=NW
)


frame_baixo = Frame(
    janela,
    width=260,
    height=300,
    bg=cor0,
    relief='flat'
)

frame_baixo.grid(
    row=1,
    column=0,
    sticky=NW
)

# ESTILO

estilo = ttk.Style(janela)

estilo.theme_use('clam')

# JOGADOR

app_pessoa = Label(
    frame_cima,
    text='JOGADOR',
    height=1,
    anchor='center',
    bg=cor1,
    fg=cor0,
    font=('Ivy', 10, 'bold')
)

app_pessoa.place(
    x=10,
    y=70
)

# BARRA DO JOGADOR

app_pessoa_linha = Label(
    frame_cima,
    text='',
    bg=cor1
)

app_pessoa_linha.place(
    x=0,
    y=0,
    width=5,
    height=80
)

# PONTOS DO JOGADOR

app_pessoa_pontos = Label(
    frame_cima,
    text='0',
    height=1,
    anchor='center',
    bg=cor1,
    fg=cor0,
    font=('Ivy', 30, 'bold')
)

app_pessoa_pontos.place(
    x=50,
    y=15
)

# SEPARADOR

app_vs = Label(
    frame_cima,
    text=':',
    height=1,
    anchor='center',
    bg=cor1,
    fg=cor0,
    font=('Ivy', 30, 'bold')
)

app_vs.place(
    x=125,
    y=15
)

# PC

app_pc = Label(
    frame_cima,
    text='PC',
    height=1,
    anchor='center',
    bg=cor1,
    fg=cor0,
    font=('Ivy', 10, 'bold')
)

app_pc.place(
    x=205,
    y=70
)

# BARRA DO PC

app_pc_linha = Label(
    frame_cima,
    text='',
    bg=cor1
)

app_pc_linha.place(
    x=255,
    y=0,
    width=5,
    height=80
)

# PONTOS DO PC

app_pc_pontos = Label(
    frame_cima,
    text='0',
    height=1,
    anchor='center',
    bg=cor1,
    fg=cor0,
    font=('Ivy', 30, 'bold')
)

app_pc_pontos.place(
    x=170,
    y=15
)

# BARRA AMARELA INFERIOR

app_empate = Label(
    frame_cima,
    text='APERTE JOGAR',
    anchor='center',
    bg=cor3,
    fg=cor1,
    font=('Ivy', 7, 'bold')
)

# IMPORTANTE:
# width = 260 pixels
# height = 15 pixels

app_empate.place(
    x=0,
    y=95,
    width=260,
    height=15
)

# JOGADA DO JOGADOR

app_jogada_pessoa = Label(
    frame_baixo,
    text='Você:',
    height=1,
    anchor='center',
    bg=cor0,
    fg=cor1,
    font=('Ivy', 10, 'bold')
)

app_jogada_pessoa.place(
    x=10,
    y=10
)

# JOGADA DO PC

app_jogada_pc = Label(
    frame_baixo,
    text='PC:',
    height=1,
    anchor='center',
    bg=cor0,
    fg=cor1,
    font=('Ivy', 10, 'bold')
)

app_jogada_pc.place(
    x=180,
    y=10
)

# RESULTADO DA RODADA

app_vencedor = Label(
    frame_baixo,
    text='',
    height=1,
    anchor='center',
    bg=cor0,
    fg=cor1,
    font=('Ivy', 10, 'bold')
)

app_vencedor.place(
    x=5,
    y=40,
    width=250
)

# VARIÁVEIS DO JOGO

pontos_pessoa = 0

pontos_pc = 0

rodadas = 5

# BOTÕES

btn_pedra = None

btn_papel = None

btn_tesoura = None

# FUNÇÃO PARA APAGAR AS BARRINHAS

def apagar_barras():

    app_pessoa_linha.config(
        bg=cor1
    )

    app_pc_linha.config(
        bg=cor1
    )

# FUNÇÃO PARA TERMINAR O JOGO

def terminar_jogo():

    global btn_pedra
    global btn_papel
    global btn_tesoura

    # Desativa os botões
    if btn_pedra is not None:
        btn_pedra.config(
            state=DISABLED
        )

    if btn_papel is not None:
        btn_papel.config(
            state=DISABLED
        )

    if btn_tesoura is not None:
        btn_tesoura.config(
            state=DISABLED
        )

    # JOGADOR VENCEU

    if pontos_pessoa > pontos_pc:

        app_vencedor.config(
            text='VOCÊ VENCEU O JOGO!',
            fg=cor4
        )

        app_empate.config(
            text='VOCÊ VENCEU!',
            bg=cor4,
            fg=cor1
        )

    # PC VENCEU

    elif pontos_pc > pontos_pessoa:

        app_vencedor.config(
            text='PC VENCEU O JOGO!',
            fg=cor5
        )

        app_empate.config(
            text='PC VENCEU!',
            bg=cor5,
            fg=cor0
        )

    # EMPATE FINAL

    else:

        app_vencedor.config(
            text='O JOGO TERMINOU EMPATADO!',
            fg=cor2
        )

        app_empate.config(
            text='EMPATE!',
            bg=cor3,
            fg=cor1
        )

# FUNÇÃO PRINCIPAL DO JOGO

def jogar(jogada):

    global pontos_pessoa
    global pontos_pc
    global rodadas

    # VERIFICA SE O JOGO ACABOU

    if rodadas <= 0:
        return

    # APAGA AS BARRAS

    apagar_barras()

    # OPÇÕES DO JOGO

    opcoes = [
        'pedra',
        'papel',
        'tesoura'
    ]

    # PC ESCOLHE

    escolha_pc = random.choice(
        opcoes
    )

    # MOSTRA AS JOGADAS

    app_jogada_pessoa.config(
        text='Você: ' + jogada
    )

    app_jogada_pc.config(
        text='PC: ' + escolha_pc
    )

    # EMPATE

    if jogada == escolha_pc:

        app_vencedor.config(
            text='EMPATE!',
            fg=cor2
        )

        app_empate.config(
            text='EMPATE',
            bg=cor3,
            fg=cor1
        )

        # AS DUAS BARRAS FICAM AMARELAS
        app_pessoa_linha.config(
            bg=cor3
        )

        app_pc_linha.config(
            bg=cor3
        )

    # JOGADOR GANHOU

    elif (
        jogada == 'pedra'
        and escolha_pc == 'tesoura'
    ) or (
        jogada == 'papel'
        and escolha_pc == 'pedra'
    ) or (
        jogada == 'tesoura'
        and escolha_pc == 'papel'
    ):

        pontos_pessoa += 1


        app_vencedor.config(
            text='VOCÊ GANHOU!',
            fg=cor4
        )

        app_empate.config(
            text='VOCÊ GANHOU',
            bg=cor4,
            fg=cor1
        )

        # BARRA DO JOGADOR ACENDE
        app_pessoa_linha.config(
            bg=cor4
        )

        # BARRA DO PC CONTINUA APAGADA
        app_pc_linha.config(
            bg=cor1
        )

    # PC GANHOU

    else:

        pontos_pc += 1


        app_vencedor.config(
            text='PC GANHOU!',
            fg=cor5
        )

        app_empate.config(
            text='PC GANHOU',
            bg=cor5,
            fg=cor0
        )

        # BARRA DO JOGADOR APAGADA
        app_pessoa_linha.config(
            bg=cor1
        )


        # BARRA DO PC ACENDE
        app_pc_linha.config(
            bg=cor5
        )

    # ATUALIZA PLACAR

    app_pessoa_pontos.config(
        text=str(pontos_pessoa)
    )

    app_pc_pontos.config(
        text=str(pontos_pc)
    )

    # DIMINUI RODADA

    rodadas -= 1

    print(
        'Rodadas restantes:',
        rodadas
    )

    # TERMINOU?

    if rodadas == 0:

        janela.after(
            1000,
            terminar_jogo
        )

# INICIAR NOVO JOGO

def iniciar_jogo():

    global pontos_pessoa
    global pontos_pc
    global rodadas

    global icone_pedra
    global icone_papel
    global icone_tesoura

    global btn_pedra
    global btn_papel
    global btn_tesoura

    # REINICIA VARIÁVEIS

    pontos_pessoa = 0

    pontos_pc = 0

    rodadas = 5

    # RESETA PLACAR

    app_pessoa_pontos.config(
        text='0'
    )

    app_pc_pontos.config(
        text='0'
    )

    # APAGA BARRAS

    apagar_barras()

    # RESETA TEXTOS
    app_jogada_pessoa.config(
        text='Você:'
    )

    app_jogada_pc.config(
        text='PC:'
    )

    app_vencedor.config(
        text=''
    )

    app_empate.config(
        text='ESCOLHA UMA JOGADA',
        bg=cor3,
        fg=cor1
    )

    # CARREGA PEDRA
   
    icone_pedra = Image.open(
        'pedra.png'
    )

    icone_pedra = icone_pedra.resize(
        (50, 50),
        Image.Resampling.LANCZOS
    )

    icone_pedra = ImageTk.PhotoImage(
        icone_pedra
    )


    btn_pedra = Button(
        frame_baixo,
        width=50,
        height=50,
        image=icone_pedra,
        bg=cor0,
        activebackground=cor0,
        relief='flat',
        bd=0,
        command=lambda: jogar('pedra')
    )

    btn_pedra.place(
        x=25,
        y=60
    )

    # CARREGA PAPEL

    icone_papel = Image.open(
        'papel.png'
    )

    icone_papel = icone_papel.resize(
        (50, 50),
        Image.Resampling.LANCZOS
    )

    icone_papel = ImageTk.PhotoImage(
        icone_papel
    )

    btn_papel = Button(
        frame_baixo,
        width=50,
        height=50,
        image=icone_papel,
        bg=cor0,
        activebackground=cor0,
        relief='flat',
        bd=0,
        command=lambda: jogar('papel')
    )

    btn_papel.place(
        x=100,
        y=60
    )


    # CARREGA TESOURA
    
    icone_tesoura = Image.open(
        'tesoura.png'
    )

    icone_tesoura = icone_tesoura.resize(
        (50, 50),
        Image.Resampling.LANCZOS
    )

    icone_tesoura = ImageTk.PhotoImage(
        icone_tesoura
    )

    btn_tesoura = Button(
        frame_baixo,
        width=50,
        height=50,
        image=icone_tesoura,
        bg=cor0,
        activebackground=cor0,
        relief='flat',
        bd=0,
        command=lambda: jogar('tesoura')
    )

    btn_tesoura.place(
        x=170,
        y=60
    )

    # MUDA BOTÃO
  
    btn_jogar.config(
        text='Novo Jogo'
    )

# BOTÃO JOGAR


btn_jogar = Button(
    frame_baixo,
    text='Jogar',
    width=40,
    height=2,
    anchor='center',
    bg=cor1,
    fg=cor0,
    activebackground=cor2,
    activeforeground=cor1,
    command=iniciar_jogo
)

btn_jogar.place(
    x=0,
    y=140
)

# INICIA O PROGRAMA

janela.mainloop()