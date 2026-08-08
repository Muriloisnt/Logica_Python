import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Cadastro")
root.geometry("1000x600")

try:
    minha_imagem = tk.PhotoImage(file="perfil.png")
    tk.Label(root, image=minha_imagem).grid(row=0, column=0)
except:
    label_imagem = tk.Label(root, text="Imagem não encontrada")



frame_cadastro = tk.Frame(root)
frame_cadastro.grid(row=0, column=1, padx=80, pady=50)


tk.Label(
    frame_cadastro,
    text="Cadastro",
    font=("Arial", 25, "bold")
).grid(row=0, column=0, columnspan=2, pady=20)


tk.Label(frame_cadastro, text="Nome:").grid(row=1, column=0, sticky="w")
nome = tk.Entry(frame_cadastro, width=30)
nome.grid(row=1, column=1, pady=5)


tk.Label(frame_cadastro, text="Gênero:").grid(row=2, column=0, sticky="w")
genero = ttk.Combobox(
    frame_cadastro,
    values=["Masculino", "Feminino"],
    width=27,
    state="readonly"
)
genero.grid(row=2, column=1, pady=5)
genero.current(0)


tk.Label(frame_cadastro, text="Cor dos Olhos:").grid(row=3, column=0, sticky="w")
olhos = ttk.Combobox(
    frame_cadastro,
    values=["Azul", "Verde", "Castanho"],
    width=27,
    state="readonly"
)
olhos.grid(row=3, column=1, pady=5)
olhos.current(0)


tk.Label(frame_cadastro, text="Altura (m):").grid(row=4, column=0, sticky="w")
altura = tk.Entry(frame_cadastro, width=30)
altura.grid(row=4, column=1, pady=5)


tk.Label(frame_cadastro, text="Peso (kg):").grid(row=5, column=0, sticky="w")
peso = tk.Entry(frame_cadastro, width=30)
peso.grid(row=5, column=1, pady=5)


def cadastrar():
    print("Nome:", nome.get())
    print("Gênero:", genero.get())
    print("Cor dos Olhos:", olhos.get())
    print("Altura:", altura.get())
    print("Peso:", peso.get())


tk.Button(
    frame_cadastro,
    text="Cadastrar",
    command=cadastrar
).grid(row=6, column=0, columnspan=2, pady=20)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.mainloop()