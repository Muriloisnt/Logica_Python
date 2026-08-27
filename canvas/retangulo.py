from tkinter import Tk,Canvas

janela = Tk()
canvas = Canvas(janela, width=400, height=300, bg="white")
canvas.create_rectangle(
    50, 50, 150, 100,
    fill = "blue"
)

canvas.pack()
janela.mainloop()
