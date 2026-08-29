from tkinter import Tk,Canvas

janela = Tk()

canvas = Canvas(janela, width=400, height=300, bg="black")

canvas.create_text(50, 50,text="seu texto", font=("Arial",12),fill="red")
canvas.create_text(65, 100,text="seu texto", font=("Arial",12),fill="yellow", anchor="w")
canvas.create_text(150, 150,text="seu texto", font=("Arial",12),fill="green")

canvas.pack()
janela.mainloop()
