from tkinter import Tk,Canvas
janela = Tk()

canvas = Canvas(janela, width=400, height=300, bg="white")
canvas.create_line(
    10, 10, 200, 185,
    fill="black",
    width=3
)
canvas.create_line(
    10, 200, 10, 10,
    fill="red",
    width=3
)

canvas.create_line(
    200, 10, 10, 10,
    fill="blue",
    width=3
)
canvas.pack()
janela.mainloop()