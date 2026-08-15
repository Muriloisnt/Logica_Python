# import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
 # pip install Pillow
from PIL import Image, ImageTk


#cores------------------------------
cor0 = '#FFFFFF' #white / branca 
cor1 = '#333333' #black / preta
cor2 = '#fcc058' #orange / laranja 
cor3 = '#fff873' #yellow / amarela
cor4 = '#34eb3d' #green / verde 
cor5 = '#e85151' #red / vermlha 
fundo = '#3b3b3b'



janela = Tk()
janela.title('pedra, papel e tesoura')
janela.geometry('260x280')
janela.configure(bg=fundo)

                                                                                  

frame_cima = Frame(janela, width=260, height=100, bg=cor1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260 , height=300, bg=cor0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando os jogadores 
#jogador pessoa 
app_pessoa = Label(frame_cima, text='jogador', height=1, anchor='center',
                   bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_pessoa.place(x=10, y=70)
#barra marcou pontos
app_pessoa_linha = Label(frame_cima, text="", height=10, anchor='center',
                         bg=cor4, fg=cor0, font=('Ivy 10 bold'))
app_pessoa_linha.place(x=0, y=0)
#ponuação
app_pessoa_pontos = Label(frame_cima, text='0', height=1, anchor='center',
                          bg=cor1, fg=cor0, font=('Ivy 30 bold'))
app_pessoa_pontos.place(x=50, y=20)

#sepação da pontuação
app_vs = Label(frame_cima, text=':', height=1, anchor='center',
               bg=cor1, fg=cor0, font=('Ivy 30 bold'))
app_vs.place(x=125, y=20)

#jogador-pc
app_pc = Label(frame_cima, text='PC', height=1, anchor='center',
                bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_pc.place(x=205, y=70)
#barra marcou pontos
app_pc_linha = Label(frame_cima, text="", height=10, anchor="center", bg=cor4,
                     fg=cor0, font=("Ivy 10 bold"))
app_pc_linha.place(x=255, y=0)
#pontuaçao
app_pc_pontos = Label(frame_cima, text="0", height=1, anchor="center",
                      bg=cor1, fg=cor0, font=("Ivy 30 bold"))
app_pc_pontos.place(x=170, y=20)

#barra de empate
app_empate = Label(frame_cima, text="",width=255, anchor="center",
                   bg=cor3, fg=cor0, font=("Ivy 1 bold"))
app_empate.place(x=0,y=95)

#mostra jogada do pc
app_jogada_pc = Label(frame_baixo, text="", height=1, anchor="center",
                      bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pc.place(x=190, y=10)

#mostra jogada do jogador
app_jogada_pessoa = Label(frame_baixo, text="", height=1, anchor="center",
                          bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_jogada_pessoa.place(x=10, y=10)

app_vencedor = Label(frame_baixo, text="", height=1, anchor="center",
                     bg=cor0, fg=cor1, font=("Ivy 10 bold"))
app_vencedor.palce(x=5, y=60)

global escola_pessoa
global escolha_pc
global pessoa_pontos
global pontos_pc
global rodadas
pontos_pessoa = 0
pontos_pc = 0
rodadas = 5

#funçaõ logica do jogo
def jogar (jogada):
    global pontos_pc
    global pontos_pessoa
    global rodadas
    opçoes = ["pedra", "papel", "tesoura"]


    app_pessoa_linha["bg"] = cor1
    app_pc_linha["bg"] = cor1
    app_empate["bg"] = cor0

    

    def terminar_jogo():
        pass

    if rodadas > 0:
        print(rodadas)
        escolha_pc = random.choice(opçoes)
        app_jogada_pc["text"] = escolha_pc

        escolha_pessoa = jogada
        app_jogada_pessoa["text"] = escolha_pessoa
        print(escolha_pessoa, escolha_pc)
        #tempo 1:03:26
    else:
        terminar_jogo()               


#iniciando função
def iniciar_jogo ():
    global icone_tesoura
    global icone_papel
    global icone_pedra
    global btn_tesoura
    global btn_pedra
    global btn_papel



    icone_pedra = Image.open("pedra.png")
    icone_pedra = icone_pedra.resize((50, 50),
                                    Image.Resampling.LANCZOS)
    icone_pedra = ImageTk.PhotoImage(icone_pedra)
    btn_pedra = Button(frame_baixo, width=50, height=50,
                    image=icone_pedra, bg=cor0, fg=cor0,
                    compound="center", font=("Ivy 10 bold"),
                    anchor="center", relief="flat", command=lambda: jogar("pedra"))
    btn_pedra.place(x=25, y=60)

    icone_papel = Image.open("papel.png")
    icone_papel = icone_papel.resize((50, 50),
                                    Image.Resampling.LANCZOS)
    icone_papel = ImageTk.PhotoImage(icone_papel)
    btn_papel = Button(frame_baixo, width=50, height=50,
                    image=icone_papel, bg=cor0, fg=cor0,
                    compound="center", font=("Ivy 10 bold"),
                    anchor="center", relief="flat", command=lambda: jogar("papel"))
    btn_papel.place(x=100, y=60)

    icone_tesoura = Image.open("tesoura.png")
    icone_tesoura = icone_tesoura.resize((50, 50),
                                        Image.Resampling.LANCZOS)
    icone_tesoura = ImageTk.PhotoImage(icone_tesoura)
    btn_tesoura = Button(frame_baixo, width=50, height=50,
                        image=icone_tesoura, bg=cor0, fg=cor0,
                        compound="center", font=("Ivy 10 bold"),
                        anchor="center", relief="flat", command=lambda: jogar ("tesoura"))
    btn_tesoura.place(x=170, y=60)


btn_jogar = Button(frame_baixo,text="Jogar", width= 40, height=2,
                   anchor="center", bg=cor1,
                   fg=cor0, command=iniciar_jogo)
btn_jogar.place(x=0, y=140)




janela.mainloop()