import tkinter as tk
from tkinter import ttk



cores = {
    "Preto": "black",
    "Marrom": "brown",
    "Vermelho": "red",
    "Laranja": "orange",
    "Amarelo": "yellow",
    "Verde": "green",
    "Azul": "blue",
    "Violeta": "purple",
    "Cinza": "gray",
    "Branco": "white"
}


valores = {
    "Preto": 0,
    "Marrom": 1,
    "Vermelho": 2,
    "Laranja": 3,
    "Amarelo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Cinza": 8,
    "Branco": 9
}


multiplicadores = {
    "Preto": 1,
    "Marrom": 10,
    "Vermelho": 100,
    "Laranja": 1000,
    "Amarelo": 10000,
    "Verde": 100000,
    "Azul": 1000000,
    "Violeta": 10000000,
    "Cinza": 100000000,
    "Branco": 1000000000
}


tolerancias = {
    "Marrom": 1,
    "Vermelho": 2,
    "Dourado": 5,
    "Prateado": 10
}



janela = tk.Tk()

janela.title("Calculadora de Resistores")

janela.geometry("700x500")




titulo = tk.Label(
    janela,
    text="Calculadora de Resistores",
    font=("Arial", 20)
)
titulo.pack()

por_cor = tk.Checkbutton(
    janela,
    text="resistencia por cor",
    font=("Arial", 12)
)

por_cor.pack()

por_resistencia = tk.Checkbutton(
    janela,
    text="resistencia ",
    font=("Arial", 12),
    width=4
)





janela.mainloop()