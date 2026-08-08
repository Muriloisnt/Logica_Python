import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Senai - sistemas")
root.geometry("800x600")


valor_selecionado = tk.StringVar(value="Primeiro")

def selecao_mudou(evento):
    
    selecao = combobox.get()
    label.config(text=f"{selecao} selecionado!")


combobox = ttk.Combobox(root, textvariable=valor_selecionado, values=["Primeiro", "Segundo", "Terceiro"], state="readonly")
combobox.bind("<<ComboboxSelected>>", selecao_mudou)
combobox.pack(pady=20)


label = tk.Label(root, text="Primeiro selecionado!")
label.pack(pady=20)

root.mainloop()
