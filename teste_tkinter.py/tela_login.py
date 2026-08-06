from tkinter import *
from tkinter import messagebox

# ----------------- Janela -----------------
janela = Tk()
janela.title("Tela de Login")
janela.geometry("400x500")
janela.configure(bg="#4e73df")
janela.resizable(False, False)

# ----------------- Título -----------------
titulo = Label(
    janela,
    text="Faça seu Login",
    font=("Arial", 20, "bold"),
    bg="#4e73df",
    fg="white"
)
titulo.pack(pady=20)

# ----------------- Foto -----------------
try:
    foto = PhotoImage(file="perfil.gif")   # Coloque perfil.gif na mesma pasta
    lbl_foto = Label(janela, image=foto, bg="#4e73df")
    lbl_foto.pack(pady=10)
except:
    Label(
        janela,
        text="Imagem não encontrada",
        bg="#4e73df",
        fg="white"
    ).pack()

# ----------------- Frame -----------------
frame = Frame(janela, bg="#4e73df")
frame.pack(pady=20)

# Usuário
Label(
    frame,
    text="Usuário",
    bg="#4e73df",
    fg="white",
    font=("Arial", 11)
).grid(row=0, column=0, sticky="w")

usuario = Entry(frame, width=30)
usuario.grid(row=1, column=0, pady=(0, 15))

# Senha
Label(
    frame,
    text="Senha",
    bg="#4e73df",
    fg="white",
    font=("Arial", 11)
).grid(row=2, column=0, sticky="w")

senha = Entry(frame, width=30, show="*")
senha.grid(row=3, column=0, pady=(0, 15))

# Lembre de mim
lembrar = IntVar()

Checkbutton(
    frame,
    text="Lembre de mim",
    variable=lembrar,
    bg="#4e73df",
    fg="white",
    activebackground="#4e73df",
    selectcolor="#4e73df"
).grid(row=4, column=0, sticky="w", pady=10)

# ----------------- Login -----------------
def entrar():
    if usuario.get() == "admin" and senha.get() == "1234":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

Button(
    janela,
    text="Entrar",
    command=entrar,
    width=20,
    bg="white",
    fg="#4e73df",
    font=("Arial", 11, "bold")
).pack(pady=20)

janela.mainloop()