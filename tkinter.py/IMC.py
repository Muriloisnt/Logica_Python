# Importa a biblioteca Tkinter, utilizada para criar interfaces gráficas.
# O "as tk" cria um apelido para facilitar a escrita dos comandos.
import tkinter as tk

# Função responsável por calcular o IMC quando o botão for clicado.
def calcular_imc():
    # O bloco try tenta executar o código abaixo.
    # Se ocorrer algum erro (como o usuário digitar letras),
    # o programa passará para o bloco except.
  try:
       # Obtém o valor digitado no campo de peso.
        # O método get() lê o texto da caixa de entrada.
        # O replace() troca vírgulas por pontos para aceitar números decimais.
        # O float() converte o texto para um número decimal.
    peso = float(entrada_peso.get().replace(",", "."))
    # Faz o mesmo processo para a altura.
    altura = float(entrada_altura.get().replace(",", "."))

     # Calcula o Índice de Massa Corporal (IMC).
        # A fórmula utilizada é:
        # IMC = peso / (altura²)
        # O operador ** representa potência.
    imc = peso / (altura**2)

    # Verifica em qual faixa o IMC se encontra.
    if imc < 18.5:
      mensagem = "Abaixo do peso"
    #Caso o IMC seja maior ou igual a 18.5 e menor que 25.
    elif imc < 25:
      mensagem = "Saudável"
     # Caso o IMC seja maior ou igual a 25 e menor que 30.
    elif imc < 30:
      mensagem = "Sobrepeso"
     # Caso o IMC seja maior ou igual a 30.
    else:
      mensagem = "Obesidade"
# Atualiza o texto do rótulo de resultado.
        # A f-string permite inserir valores dentro da mensagem.
        # :.2f exibe o IMC com duas casas decimais.
        # \n faz a quebra de linha.
    label_resultado.config(text=f"IMC: {imc:.2f}\nStatus: {mensagem}")
# Caso ocorra um erro ao converter os valores para números,
    # será exibida uma mensagem informando o usuário.
  except ValueError:
    
    label_resultado.config(text="Erro: Digite apenas números!")


# Cria a janela principal do programa.
janela = tk.Tk()
janela.title("Calculadora de IMC") # Define o título exibido na barra superior da janela.
janela.geometry("250x250") # Define o tamanho da janela (250 pixels de largura por 250 de altura).


label_peso = tk.Label(janela, text="Peso (kg):")# Cria um texto (Label) indicando onde o usuário deve informar o peso.
label_peso.pack(pady=5)# Posiciona o texto na janela.
# O parâmetro pady adiciona um espaço vertical de 5 pixels.
label_peso.pack(pady=5)
entrada_peso = tk.Entry(janela)# Cria a caixa de entrada onde o usuário digitará o peso.
entrada_peso.pack(pady=5)# Posiciona a caixa de entrada na janela.


label_altura = tk.Label(janela, text="Altura (M):") # Cria um texto indicando onde o usuário deve informar a altura.
label_altura.pack(pady=5) # Posiciona o texto na janela.
entrada_altura = tk.Entry(janela) # Cria a caixa de entrada para a altura.
entrada_altura.pack(pady=5) # Posiciona a caixa de entrada.



botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
# Cria o botão que executará o cálculo do IMC.
# O parâmetro command informa qual função será chamada
# quando o botão for pressionado.
botao_calcular.pack(pady=15)# Posiciona o botão na janela.


label_resultado = tk.Label(janela, text="", font=("Arial", 10, "bold")) 
# Cria um rótulo inicialmente vazio para exibir o resultado.
# Também define a fonte Arial, tamanho 10 e em negrito.
label_resultado.pack(pady=5) # Posiciona o rótulo na janela.


janela.mainloop() # Inicia o loop principal da interface gráfica.
# Mantém a janela aberta e aguardando as ações do usuário,
# como digitar informações e clicar no botão.

