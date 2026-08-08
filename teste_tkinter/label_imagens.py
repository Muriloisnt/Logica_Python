import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("SENAI - Sistemas")
root.geometry("800x600")

minha_imagem = tk.PhotoImage(file="perfil.png")

tk.Label(root, image=minha_imagem)

root.mainloop()