import tkinter as tk

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="skyblue")

frame = tk.Frame(root, width=420, height=220)
frame.pack(padx=10, pady=10)

a_frame = tk.Frame(frame, width=190, height=190, bg="green")
a_frame.pack(side="right", padx=10, pady=10)

b_frame = tk.Frame(frame,width=190, height=190, bg="green")
b_frame.pack(side="right", padx=10,pady=10)

root.mainloop()