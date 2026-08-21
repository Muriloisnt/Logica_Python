#Cópia Independente

lista = [1, 2, 3, 4, 5]
copia = lista[:]
copia[0] = 6
print(lista)
# [1, 2, 3, 4, 5]

#--------------------------------------------

#Fatiamento de Listas (Slicing)
#Use [inicio:fim] para extrair partes de uma lista.
#O índice fim é exclusivo. Significa que a sua posição não fará para da nova lista

lista = [1, 2, 3, 4, 5]

lista[0:5] # [1, 2, 3, 4, 5]
lista[:5] # [1, 2, 3, 4, 5]
lista[1:3] # [2, 3]
lista[1:4] # [2, 3, 4]
lista[3:] # [4, 5]
lista[:3] # [1, 2, 3]


#--------------------------------------------
#Índices Negativos
#Índices negativos acessam elementos a partir do final da lista.
#-1 é o último elemento, -2 o penúltimo, e assim por diante.

lista = [1, 2, 3, 4, 5]

lista[:-1] # [1, 2, 3, 4]
lista[-1] # 5
lista[-2] # 4

#--------------------------------------------
#Função len(): Tamanho da Lista

#Lista com elementos
lista = [12, 9, 5]
print(len(lista))   #3

#Lista vazia
lista2 = []
print(len(lista2))   #0


#--------------------------------------------
#len() em Laços de Repetição
lista = [10, 20, 30, 40]
for i in range(len(lista)):
    print(lista[i]) # 10, 20, 30, 40



#--------------------------------------------
#Código Robusto com len()

#Se a lista mudar de tamanho, o programa continua funcionando — os índices
#válidos vão de 0 até len(L) – 1.

L = [10, 20, 30, 40, 50]
for i in range(len(L)):
    print(L[i])

#--------------------------------------------
#Listas São Flexíveis: append()
#Listas podem crescer dinamicamente. Use append() para
#adicionar elementos ao final durante a execução.

lista = []
lista.append("a")
lista.append("b")
lista.append("c")
print(lista) # ['a', 'b', 'c']

#--------------------------------------------
#Removendo Elementos com del
#Remoção por Índice
#A instrução del remove um elemento pela sua posição. A
#lista é reorganizada automaticamente após a exclusão.

lista = ["a", "b", "c"]
del lista[1]
print(lista) # ['a', 'c']
del lista[0]
print(lista) # ['c']
#--------------------------------------------
#Removendo Fatias Inteiras
#Também é possível apagar um intervalo de elementos de
#uma só vez usando slicing:
lista = ["a", "b", "c", "d", "e", "f"]
del lista[1:5]
print(lista) # ['a', 'f']

#--------------------------------------------
#Leitura de Números até Zero
numeros = []

while True:
    valor = int(input("Digite um número(0 para sair): "))

if valor == 0:
    break

numeros.append(valor)

print("Lista completa:", numeros)

#--------------------------------------------
#Imprimir Números um por Vez

numeros = []
while True:
    valor = int(input("Digite um número(0 para sair): "))
if valor == 0:
    break

    numeros.append(valor)

for numero in numeros:
    print(numero)

#--------------------------------------------

#Encontrar Menor e Maior Valor
numeros = []
while True:
    valor = int(input("Digite um número(0 para sair): "))
    if valor == 0:
        break
    numeros.append(valor)

menor = min(numeros)
print("Menor:", menor)
maior = max(numeros)
print("Maior:", maior)