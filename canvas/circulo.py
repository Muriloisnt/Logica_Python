from tkinter import Tk,Canvas

janela = Tk()
canvas = Canvas(janela, width=400, height=300, bg="white")

Canvas = canvas.create_oval(50, 50, 150,
                            150,fill="yellow")
Canvas = canvas.create_oval(200, 200, 400, 250, fill="green")

canvas.pack()
janela.mainloop()