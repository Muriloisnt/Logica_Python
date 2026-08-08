import tkinter as tk
from tkinter import ttk
root = tk.Tk ()
root.title("Senai - sistemas")
root.geometry("800x600")

checkbox_estado = tk.IntVar()

def mostrar_estado():
    if checkbox_estado.get():
        txt = "Checked"
    else:
        txt = "Unchecked"
    checkbox.config (
        text=f"Check me!  ({txt})")

    checkbox = tk.Checkbutton (root,
        text="Check me! (checked)",
        variable=checkbox_estado,
        command=mostrar_estado)  
    checkbox.select()
    checkbox.pack(expand=True)
    
    root.mainloop()

