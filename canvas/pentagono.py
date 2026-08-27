from tkinter import Tk,Canvas
janela = Tk()

canvas = Canvas(janela, width=400, height=300, bg="black")
canvas.create_polygon(
    60, 50,
    10, 100,
    40, 150,
    80, 150,
    110, 100,
    fill="green",
   outline="white",
   width=2
)
canvas.pack()
janela.mainloop()