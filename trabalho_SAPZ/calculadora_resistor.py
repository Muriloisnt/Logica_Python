import tkinter as tk
from tkinter import ttk, messagebox



cores = {
    "preto": 0,
    "marrom": 1,
    "vermelho": 2,
    "laranja": 3,
    "amarelo": 4,
    "verde": 5,
    "azul": 6,
    "violeta": 7,
    "cinza": 8,
    "branco": 9
}

multiplicadores = {
    "preto": 1,
    "marrom": 10,
    "vermelho": 100,
    "laranja": 1000,
    "amarelo": 10000,
    "verde": 100000,
    "azul": 1000000,
    "violeta": 10000000,
    "cinza": 100000000,
    "branco": 1000000000,
    "dourado": 0.1,
    "prateado": 0.01
}

tolerancias = {
    "marrom": 1,
    "vermelho": 2,
    "verde": 0.5,
    "azul": 0.25,
    "violeta": 0.1,
    "cinza": 0.05,
    "dourado": 5,
    "prateado": 10
}


cores_visuais = {
    "preto": "#111111",
    "marrom": "#6B3E1E",
    "vermelho": "#EF2027",
    "laranja": "#F39C12",
    "amarelo": "#F1D32F",
    "verde": "#2E9952",
    "azul": "#2676B5",
    "violeta": "#813FA8",
    "cinza": "#888888",
    "branco": "#F4F4F4",
    "dourado": "#D4A72C",
    "prateado": "#BDBDBD"
}




def formatar_resistencia(valor):
    """Converte o valor para Ω, kΩ ou MΩ."""

    if valor >= 1000000:
        return f"{valor / 1000000:.2f} MΩ"

    elif valor >= 1000:
        return f"{valor / 1000:.2f} kΩ"

    else:
        return f"{valor:.2f} Ω"


def pegar_cor(numero):
    

    for cor, valor in cores.items():
        if valor == numero:
            return cor

    return None




janela = tk.Tk()

janela.title("Calculadora de Resistor")

# Tamanho parecido com o exemplo
janela.geometry("760x650")

janela.resizable(False, False)

janela.configure(
    bg="#EAF2F7"
)



titulo = tk.Label(
    janela,
    text="Calculadora de Resistor",
    font=("Arial", 20, "bold"),
    fg="#263E53",
    bg="#EAF2F7"
)

titulo.place(
    x=45,
    y=35
)


painel = tk.Frame(
    janela,
    bg="white"
)

painel.place(
    x=35,
    y=80,
    width=690,
    height=540
)



grupo_modo = tk.LabelFrame(
    painel,
    text="Como deseja informar o resistor?",
    font=("Arial", 10, "bold"),
    fg="#263B4A",
    bg="white",
    bd=1,
    relief="groove"
)

grupo_modo.place(
    x=15,
    y=15,
    width=660,
    height=65
)


modo = tk.StringVar()

modo.set("cores")


radio_valor = tk.Radiobutton(
    grupo_modo,
    text="Valor da resistência",
    variable=modo,
    value="valor",
    command=lambda: mudar_modo(),
    bg="white",
    activebackground="white",
    font=("Arial", 9)
)

radio_valor.place(
    x=10,
    y=23
)


radio_cores = tk.Radiobutton(
    grupo_modo,
    text="Cores do resistor",
    variable=modo,
    value="cores",
    command=lambda: mudar_modo(),
    bg="white",
    activebackground="white",
    font=("Arial", 9)
)

radio_cores.place(
    x=145,
    y=23
)

frame_cores = tk.Frame(
    painel,
    bg="white"
)

frame_cores.place(
    x=20,
    y=95,
    width=650,
    height=75
)




tk.Label(
    frame_cores,
    text="Banda 1:",
    font=("Arial", 9),
    fg="#34495E",
    bg="white"
).place(
    x=5,
    y=0
)

banda1 = ttk.Combobox(
    frame_cores,
    values=list(cores.keys()),
    state="readonly",
    width=14
)

banda1.place(
    x=5,
    y=23
)




tk.Label(
    frame_cores,
    text="Banda 2:",
    font=("Arial", 9),
    fg="#34495E",
    bg="white"
).place(
    x=140,
    y=0
)

banda2 = ttk.Combobox(
    frame_cores,
    values=list(cores.keys()),
    state="readonly",
    width=14
)

banda2.place(
    x=140,
    y=23
)




tk.Label(
    frame_cores,
    text="Multiplicador:",
    font=("Arial", 9),
    fg="#34495E",
    bg="white"
).place(
    x=275,
    y=0
)

multiplicador = ttk.Combobox(
    frame_cores,
    values=list(multiplicadores.keys()),
    state="readonly",
    width=14
)

multiplicador.place(
    x=275,
    y=23
)



tk.Label(
    frame_cores,
    text="Tolerância:",
    font=("Arial", 9),
    fg="#34495E",
    bg="white"
).place(
    x=410,
    y=0
)

tolerancia_cores = ttk.Combobox(
    frame_cores,
    values=list(tolerancias.keys()),
    state="readonly",
    width=14
)

tolerancia_cores.place(
    x=410,
    y=23
)




frame_valor = tk.Frame(
    painel,
    bg="white"
)




tk.Label(
    frame_valor,
    text="Valor da resistência (Ω):",
    font=("Arial", 9),
    fg="#34495E",
    bg="white"
).place(
    x=5,
    y=0
)

entrada_valor = tk.Entry(
    frame_valor,
    width=21,
    font=("Arial", 10)
)

entrada_valor.place(
    x=5,
    y=23,
    height=25
)



tk.Label(
    frame_valor,
    text="Tolerância:",
    font=("Arial", 9),
    fg="#34495E",
    bg="white"
).place(
    x=190,
    y=0
)

tolerancia_valor = ttk.Combobox(
    frame_valor,
    values=list(tolerancias.keys()),
    state="readonly",
    width=14
)

tolerancia_valor.place(
    x=190,
    y=23
)




label_resultado = tk.Label(
    painel,
    text="Digite o valor da resistência ou selecione as cores.",
    font=("Arial", 10, "bold"),
    fg="#20384D",
    bg="white"
)

label_resultado.place(
    x=20,
    y=215
)



canvas = tk.Canvas(
    painel,
    width=630,
    height=250,
    bg="#F7F9FA",
    highlightthickness=1,
    highlightbackground="#D5DDE3"
)

canvas.place(
    x=20,
    y=245
)



def desenhar_resistor(faixas=None):

    canvas.delete("all")

  

    if faixas is None:

        canvas.create_text(
            315,
            125,
            text="Aguarde a seleção do modo",
            font=("Arial", 10),
            fill="#888888"
        )

        return



    canvas.create_text(
        315,
        35,
        text="Resistor de 4 faixas",
        font=("Arial", 14, "bold"),
        fill="#202020"
    )

  

    canvas.create_line(
        0,
        120,
        130,
        120,
        fill="#777777",
        width=6
    )

   

    canvas.create_line(
        500,
        120,
        630,
        120,
        fill="#777777",
        width=6
    )

  

    canvas.create_rectangle(
        130,
        90,
        500,
        150,
        fill="#F1E3B8",
        outline="#6D5B39",
        width=2
    )



    posicoes = [190, 250, 310, 370]

    for i in range(4):

        cor = faixas[i]

        canvas.create_rectangle(
            posicoes[i],
            91,
            posicoes[i] + 18,
            149,
            fill=cores_visuais[cor],
            outline="#555555",
            width=1
        )

        canvas.create_text(
            posicoes[i] + 9,
            185,
            text=cor.capitalize(),
            font=("Arial", 9),
            fill="#333333"
        )




def mudar_modo():

    # Primeiro esconde tudo
    frame_cores.place_forget()
    frame_valor.place_forget()

    if modo.get() == "cores":

        
        frame_cores.place(
            x=20,
            y=95,
            width=650,
            height=75
        )

        botao.config(
            text="Calcular resistência"
        )

    else:

        
        frame_valor.place(
            x=20,
            y=95,
            width=650,
            height=75
        )

        botao.config(
            text="Calcular cores"
        )

    label_resultado.config(
        text="Digite o valor da resistência ou selecione as cores."
    )

    desenhar_resistor(None)



def calcular_resistencia():

    cor1 = banda1.get()
    cor2 = banda2.get()
    cor_mult = multiplicador.get()
    cor_tol = tolerancia_cores.get()

    if not cor1 or not cor2 or not cor_mult or not cor_tol:

        messagebox.showwarning(
            "Atenção",
            "Selecione todas as cores do resistor."
        )

        return

    primeiro_numero = cores[cor1]
    segundo_numero = cores[cor2]

    valor_multiplicador = multiplicadores[cor_mult]
    valor_tolerancia = tolerancias[cor_tol]

    resistencia = (
        primeiro_numero * 10 + segundo_numero
    ) * valor_multiplicador

    resultado = formatar_resistencia(resistencia)

    label_resultado.config(
        text=f"Resistência: {resultado} ±{valor_tolerancia}%"
    )

    desenhar_resistor([
        cor1,
        cor2,
        cor_mult,
        cor_tol
    ])



def calcular_cores():

    texto = entrada_valor.get().strip()

    if texto == "":

        messagebox.showwarning(
            "Atenção",
            "Digite o valor da resistência."
        )

        return

    try:

        valor = float(
            texto.replace(",", ".")
        )

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Digite somente números.\n\nExemplo: 3300"
        )

        return

    if valor <= 0:

        messagebox.showwarning(
            "Atenção",
            "O valor deve ser maior que zero."
        )

        return

    cor_tolerancia = tolerancia_valor.get()

    if not cor_tolerancia:

        messagebox.showwarning(
            "Atenção",
            "Selecione a tolerância."
        )

        return

    valor_tolerancia = tolerancias[cor_tolerancia]

    encontrou = False

 

    for cor_mult, valor_mult in multiplicadores.items():

        numero = valor / valor_mult

        if 10 <= numero <= 99:

            numero = round(numero)

            if abs((numero * valor_mult) - valor) < 0.000001:

                primeiro = numero // 10
                segundo = numero % 10

                cor1 = pegar_cor(primeiro)
                cor2 = pegar_cor(segundo)

                if cor1 and cor2:

                    encontrou = True
                    break

    if not encontrou:

        messagebox.showerror(
            "Erro",
            "Esse valor não pode ser representado "
            "com um resistor de 4 faixas."
        )

        return

    resultado = formatar_resistencia(valor)

    label_resultado.config(
        text=f"Resistência: {resultado} ±{valor_tolerancia}%"
    )

    desenhar_resistor([
        cor1,
        cor2,
        cor_mult,
        cor_tolerancia
    ])



def calcular():

    if modo.get() == "cores":

        calcular_resistencia()

    else:

        calcular_cores()


botao = tk.Button(
    painel,
    text="Calcular resistência",
    command=calcular,
    bg="#4DB3A5",
    fg="white",
    activebackground="#3E988D",
    activeforeground="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2",
    padx=10,
    pady=5
)

botao.place(
    x=20,
    y=175
)



banda1.set("vermelho")
banda2.set("vermelho")
multiplicador.set("laranja")
tolerancia_cores.set("violeta")

tolerancia_valor.set("dourado")


desenhar_resistor(None)


janela.mainloop()
