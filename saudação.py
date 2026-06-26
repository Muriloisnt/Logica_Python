def saudaçao(nome='Visitante'):
    """Função que recebe um nome e retorna uma saudaçao"""
    return f'Olá, {nome} !'

print(saudaçao("Alice"))
print(saudaçao())


def calcular_media(lista):
    
    soma_total = sum(lista)
    
  
    quantidade = len(lista)
    
    media = soma_total / quantidade
    
    
    return media

minha_lista = [7, 8, 9, 10]
resultado = calcular_media(minha_lista)

print(resultado)  

