def calcular_imc():
  try:
    
    peso = float(entrada_peso.get().replace(",", "."))
    altura = float(entrada_altura.get().replace(",", "."))

    
    imc = peso / (altura**2)

   
    if imc < 18.5:
      mensagem = "Abaixo do peso"
    elif imc < 25:
      mensagem = "Saudável"
    elif imc < 30:
      mensagem = "Sobrepeso"
    else:
      mensagem = "Obesidade"

    label_resultado.config(text=f"IMC: {imc:.2f}\nStatus: {mensagem}")

  except ValueError:
    
    label_resultado.config(text="Erro: Digite apenas números!")