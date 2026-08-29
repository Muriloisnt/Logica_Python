from tkinter import Tk, Canvas

janela = Tk()


canvas = Canvas(janela, width=400, height=300, bg="light green")

canvas.create_rectangle(120,
                        140,
                        280,
                        260,
                        fill="blue")


canvas.create_polygon(
            200,
            60,
            290,
            140,
            110,
            140,
            fill="red")

canvas.create_rectangle(
    170, 
    190, 
    210, 
    260,
    fill="yellow")


canvas.create_rectangle(
    230,
    170,
    260,
    200,
    fill="green")

Canvas = canvas.create_oval(100, 5, 50, 40, fill="yellow")

Canvas = canvas.create_oval(200, 230, 210, 220, fill="black")


canvas.create_rectangle(
    130,
    170,
    160,
    200,
    fill="green")

from tkinter import Tk, Canvas

janela = Tk()
canvas = Canvas(janela, width=500, height=300, bg="light green") 


from tkinter import Tk, Canvas

janela = Tk()
canvas = Canvas(janela, width=500, height=300, bg="light green")


canvas.create_oval(50, 5, 100, 40, fill="yellow", outline="")

canvas.create_rectangle(120, 140, 280, 260, fill="blue")
canvas.create_polygon(200, 60, 290, 140, 110, 140, fill="red")


canvas.create_rectangle(170, 190, 210, 260, fill="yellow") 
canvas.create_oval(200, 220, 210, 230, fill="black")      
canvas.create_rectangle(230, 170, 260, 200, fill="green") 
canvas.create_rectangle(130, 170, 160, 200, fill="green") 


canvas.create_polygon(310, 210, 335, 180, 395, 180, 420, 210, fill="dark blue", outline="")


canvas.create_rectangle(300, 210, 430, 250, fill="dark blue", outline="") 


canvas.create_rectangle(295, 235, 300, 250, fill="black")
canvas.create_rectangle(430, 235, 435, 250, fill="black")

canvas.create_polygon(318, 208, 338, 185, 362, 185, 362, 208, fill="light blue", outline="white")
canvas.create_polygon(366, 208, 366, 185, 392, 185, 412, 208, fill="light blue", outline="white")


canvas.create_line(364, 185, 364, 248, fill="black", width=1)
canvas.create_rectangle(372, 215, 382, 218, fill="silver", outline="") 


canvas.create_oval(320, 235, 350, 265, fill="black")
canvas.create_oval(328, 243, 342, 257, fill="silver")

canvas.create_oval(385, 235, 415, 265, fill="black")
canvas.create_oval(393, 243, 407, 257, fill="silver")


canvas.create_rectangle(423, 215, 430, 223, fill="yellow", outline="") 
canvas.create_rectangle(300, 215, 305, 223, fill="red", outline="")    

canvas.pack()
janela.mainloop()
