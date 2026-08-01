import tkinter as tk

janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry("300x250")


label_usuario = tk.Label(
    janela,
    text="Usuário:",
    anchor="w"
)

label_usuario.pack(fill="x")

entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

label_usuario.pack()
label_senha = tk.Label(janela, text="Senha:")
label_senha.pack()


entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

entrada_senha = tk.Entry(janela)
entrada_senha.pack()

janela.mainloop()
