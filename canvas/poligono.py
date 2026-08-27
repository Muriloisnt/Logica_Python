from tkinter import Tk,Canvas
janela = Tk()

canvas = Canvas(janela, width=400, height=300, bg="black")
canvas.create_polygon(
    100, 50,
    150, 150,
    50, 150,
    fill="green",
   outline="white",
   width=2
)
canvas.pack()
janela.mainloop()