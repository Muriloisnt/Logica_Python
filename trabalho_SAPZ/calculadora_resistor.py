import tkinter as tk
from tkinter import ttk


cores = {
    "Preto": "black",
    "Marrom": "brown",
    "Vermelho": "red",
    "Laranja": "orange",
    "Amarelo": "yellow",
    "Verde": "green",
    "Azul": "blue",
    "Violeta": "purple",
    "Cinza": "gray",
    "Branco": "white"
}


valores = {
    "Preto": 0,
    "Marrom": 1,
    "Vermelho": 2,
    "Laranja": 3,
    "Amarelo": 4,
    "Verde": 5,
    "Azul": 6,
    "Violeta": 7,
    "Cinza": 8,
    "Branco": 9
}


multiplicadores = {
    "Preto": 1,
    "Marrom": 10,
    "Vermelho": 100,
    "Laranja": 1000,
    "Amarelo": 10000,
    "Verde": 100000,
    "Azul": 1000000,
    "Violeta": 10000000,
    "Cinza": 100000000,
    "Branco": 1000000000
}


tolerancias = {
    "Marrom": 1,
    "Vermelho": 2,
    "Dourado": 5,
    "Prateado": 10
}



janela = tk.Tk()

janela.title("Calculadora de Resistores")
janela.geometry("900x700")


titulo = tk.Label(
    janela,
    text="Calculadora de Resistores",
    font=("Arial", 20)
)

titulo.pack(pady=15)



modo = tk.StringVar(value="cor")


tk.Label(
    janela,
    text="Escolha como deseja calcular:",
    font=("Arial", 12)
).pack()


frame_modo = tk.Frame(janela)
frame_modo.pack(pady=10)


tk.Radiobutton(
    frame_modo,
    text="Escolher pelas cores",
    variable=modo,
    value="cor",
    command=lambda: mudar_modo()
).grid(row=0, column=0, padx=15)


tk.Radiobutton(
    frame_modo,
    text="Informar valor da resistência",
    variable=modo,
    value="valor",
    command=lambda: mudar_modo()
).grid(row=0, column=1, padx=15)



frame = tk.Frame(janela)
frame.pack(pady=5)


cor1 = tk.StringVar(value="Marrom")
cor2 = tk.StringVar(value="Preto")
cor3 = tk.StringVar(value="Vermelho")
cor4 = tk.StringVar(value="Dourado")


tk.Label(
    frame,
    text="1ª faixa"
).grid(row=0, column=0)


combo1 = ttk.Combobox(
    frame,
    textvariable=cor1,
    values=list(cores.keys()),
    state="readonly",
    width=12
)

combo1.grid(row=1, column=0, padx=5)


tk.Label(
    frame,
    text="2ª faixa"
).grid(row=0, column=1)


combo2 = ttk.Combobox(
    frame,
    textvariable=cor2,
    values=list(cores.keys()),
    state="readonly",
    width=12
)

combo2.grid(row=1, column=1, padx=5)


tk.Label(
    frame,
    text="Multiplicador"
).grid(row=0, column=2)


combo3 = ttk.Combobox(
    frame,
    textvariable=cor3,
    values=list(cores.keys()),
    state="readonly",
    width=12
)

combo3.grid(row=1, column=2, padx=5)


tk.Label(
    frame,
    text="Tolerância"
).grid(row=0, column=3)


combo4 = ttk.Combobox(
    frame,
    textvariable=cor4,
    values=list(tolerancias.keys()),
    state="readonly",
    width=12
)

combo4.grid(row=1, column=3, padx=5)



frame_valor = tk.Frame(janela)


tk.Label(
    frame_valor,
    text="Digite o valor da resistência:",
    font=("Arial", 12)
).pack(pady=5)


entrada_valor = tk.Entry(
    frame_valor,
    font=("Arial", 14),
    justify="center",
    width=20
)

entrada_valor.pack(pady=5)


tk.Label(
    frame_valor,
    text="Exemplo: 470, 1000, 4700, 100000",
    fg="gray"
).pack()



canvas = tk.Canvas(
    janela,
    width=600,
    height=200,
    bg="white"
)

canvas.pack(pady=20)


def desenhar():

    canvas.delete("all")

    
    canvas.create_line(
        50, 100,
        180, 100,
        width=4
    )


    canvas.create_rectangle(
        180, 60,
        480, 140,
        fill="beige",
        outline="black"
    )

    
    canvas.create_line(
        480, 100,
        550, 100,
        width=4
    )

    canvas.create_rectangle(
        220, 60,
        245, 140,
        fill=cores.get(cor1.get(), "black"),
        outline="black"
    )

    canvas.create_rectangle(
        270, 60,
        295, 140,
        fill=cores.get(cor2.get(), "black"),
        outline="black"
    )

  
    canvas.create_rectangle(
        320, 60,
        345, 140,
        fill=cores.get(cor3.get(), "black"),
        outline="black"
    )

    cor_tolerancia = {
        "Marrom": "brown",
        "Vermelho": "red",
        "Dourado": "gold",
        "Prateado": "silver"
    }

    canvas.create_rectangle(
        420, 60,
        445, 140,
        fill=cor_tolerancia.get(
            cor4.get(),
            "gold"
        ),
        outline="black"
    )





def formatar_valor(valor):

    if valor < 1000:

        return f"{valor:g} Ω"

    elif valor < 1000000:

        return f"{valor / 1000:g} kΩ"

    else:

        return f"{valor / 1000000:g} MΩ"



def valor_para_cores(valor):

    # Verifica se é inteiro
    if valor != int(valor):
        return None

    valor = int(valor)

    if valor <= 0:
        return None


    multiplicador = 0
    numero = valor

    while numero >= 100:

        if numero % 10 != 0:
            break

        numero //= 10
        multiplicador += 1

    
    while numero >= 100:

        if numero % 10 != 0:
            return None

        numero //= 10
        multiplicador += 1

    primeiro = numero // 10
    segundo = numero % 10

    if primeiro > 9 or segundo > 9:
        return None

  
    cor_multiplicador = None

    for cor, mult in multiplicadores.items():

        if mult == 10 ** multiplicador:

            cor_multiplicador = cor
            break

    if cor_multiplicador is None:
        return None


    cor_primeiro = None
    cor_segundo = None

    for cor, valor_cor in valores.items():

        if valor_cor == primeiro:
            cor_primeiro = cor

        if valor_cor == segundo:
            cor_segundo = cor

    return (
        cor_primeiro,
        cor_segundo,
        cor_multiplicador
    )



def calcular_por_cor():

    primeiro = valores[cor1.get()]

    segundo = valores[cor2.get()]

    multiplicador = multiplicadores[cor3.get()]

    tolerancia = tolerancias.get(
        cor4.get(),
        20
    )

    valor = (
        primeiro * 10 + segundo
    ) * multiplicador

    texto = formatar_valor(valor)

    resultado.config(
        text=f"Resistência: {texto} ± {tolerancia}%"
    )

    desenhar()



def calcular_por_valor():

    try:

        
        texto = entrada_valor.get().replace(",", ".")

        valor = float(texto)

        if valor <= 0:
            resultado.config(
                text="Digite um valor maior que zero."
            )
            return

        cores_resultado = valor_para_cores(valor)

        if cores_resultado is None:

            resultado.config(
                text="Esse valor não pode ser representado "
                     "com 3 faixas."
            )

            return

        primeira, segunda, multiplicador = cores_resultado

  
        cor1.set(primeira)
        cor2.set(segunda)
        cor3.set(multiplicador)

        cor4.set("Dourado")

        resultado.config(
            text=f"Resistência: {formatar_valor(valor)} ± 5%"
        )

        desenhar()

    except ValueError:

        resultado.config(
            text="Digite um valor válido."
        )



def calcular():

    if modo.get() == "cor":

        calcular_por_cor()

    else:

        calcular_por_valor()


botao = tk.Button(
    janela,
    text="CALCULAR",
    command=calcular,
    font=("Arial", 11, "bold"),
    width=15
)

botao.pack(pady=5)




resultado = tk.Label(
    janela,
    text="Resistência: 1000 Ω ± 5%",
    font=("Arial", 14)
)

resultado.pack(pady=15)



def mudar_modo():

    if modo.get() == "cor":

        frame.pack(pady=5)
        frame_valor.pack_forget()

        resultado.config(
            text="Escolha as cores e clique em CALCULAR."
        )

    else:

        frame.pack_forget()
        frame_valor.pack(pady=5)

        resultado.config(
            text="Digite o valor e clique em CALCULAR."
        )



desenhar()

janela.mainloop()
