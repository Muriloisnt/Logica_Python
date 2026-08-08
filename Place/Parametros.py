import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.title("SENAI - DESENVOLVIMENTO DE SISTEMAS")
root.geometry("300x300+50+100")

def mostrar_selecao(event):
    selecao = cidades.curselection()
    messagebox.showinfo("seleção", cidades.get(selecao))

tk.Label(root, text="Qual cidade você gostaria de cohecer?").place(x=50, y=20)

cidades = tk.Listbox(root, selectmode=tk.BROWSE, width=24)
cidades.place(x=40, y=65)

for cidade in ["Brasilia", "Floerianopolis", "Poerto Alegre", "Rio de janeiro", "Sao Paulo"]:
    cidades.insert(tk.END, cidade)

cidades.bind("<<ListboxSelect>>", mostrar_selecao)

botao = tk.Button(root , text="sair", command=quit)
botao.place(x=125, y=250)


root.mainloop()