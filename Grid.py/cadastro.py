import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("Cadastro")
root.geometry("1000x600")



frame_imagem = tk.Frame(root)
frame_imagem.grid(row=0, column=0, padx=80, pady=80)



minha_imagem = tk.PhotoImage(file="perfil.png")

label_imagem = tk.Label(
    frame_imagem,
    image=minha_imagem
)

label_imagem.image = minha_imagem

label_imagem.grid(row=0, column=0)



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
    values=["Masculino", "Feminino", "Outro"],
    width=27
)

genero.grid(row=2, column=1, pady=5)


tk.Label(frame_cadastro, text="Cor dos Olhos:").grid(row=3, column=0, sticky="w")
olhos = tk.Entry(frame_cadastro, width=30)
olhos.grid(row=3, column=1, pady=5)


tk.Label(frame_cadastro, text="Altura:").grid(row=4, column=0, sticky="w")
altura = tk.Entry(frame_cadastro, width=30)
altura.grid(row=4, column=1, pady=5)


tk.Label(frame_cadastro, text="Peso:").grid(row=5, column=0, sticky="w")
peso = tk.Entry(frame_cadastro, width=30)
peso.grid(row=5, column=1, pady=5)


tk.Button(
    frame_cadastro,
    text="Cadastrar"
).grid(row=6, column=0, columnspan=2, pady=20)



root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


root.mainloop()