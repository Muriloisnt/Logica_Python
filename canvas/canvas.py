#importar
from tkinter import Tk,Canvas 
#criar janela 
Janela = Tk()
Janela.geometry("500x400")
#criar canvas
canvas = Canvas(Janela, width=400, height=300, bg="yellow")
#exibir
canvas.pack()
Janela.mainloop()