#Implementando Pilhas em Python
#A forma mais simples de criar uma pilha é usando uma lista com os métodos append() e pop():

pilha = [] # Cria pilha vazia
pilha.append(1) # Push
pilha.append(2) # Push
pilha.append(3) # Push
print(pilha) # [1, 2, 3]

topo = pilha.pop() # Pop → 3
print(topo) # 3
print(pilha) # [1, 2]

#--------------------------------------------
#Push (Empilhar)
#Adiciona um elemento ao topo da pilha.

#Pop (Desempilhar)
#Remove e retorna o elemento do topo.

#Peek (Espiar)
#Visualiza o topo sem removê-lo.

#isEmpty
#Verifica se a pilha está vazia.

#--------------------------------------------

#Exemplo Prático: Inverter uma String
#Uma aplicação clássica de pilhas é inverter a ordem dos caracteres de uma string:

texto = "Python"
pilha = []
# Empilha cada caractere
for char in texto:
    pilha.append(char)
resultado = ""
# Desempilha na ordem inversa
while pilha:
    resultado += pilha.pop()
print(resultado)

# Saída: "nohtyP"

#--------------------------------------------
fila = []

# Adicionando 3 nomes
for i in range(3):
    nome = input("Digite um nome: ")
fila.append(nome)

# Removendo o primeiro
if fila:
    removido = fila.pop(0)
    print(f"\nRemovido: {removido}")
else:
    print("Fila vazia!")

# Mostrando fila atual
print("Fila atual:", fila)


#--------------------------------------------
fila = []
while True:
    print("\n1- Adicionar pessoa")
    print("2- Atender pessoa")
    print("3- Sair")

    opcao = input("Escolha: ")
    if opcao == "1":
        nome = input("Nome: ")
        fila.append(nome)
    elif opcao == "2":
        if not fila:
            print("Fila vazia!")
        else:
            print(f"Atendendo: {fila.pop(0)}")
    elif opcao == "3":
        break
else:
    print("Opção inválida!")

#--------------------------------------------

pilha = []

# Empilhando 5 números
for i in range(5):
    num = int(input("Digite um número: "))
pilha.append(num)
# Desempilhando 2 números
for i in range(2):
    if pilha:
        removido = pilha.pop()
        print(f"Removido: {removido}")
else:
    print("Pilha vazia!")

# Estado final
print("Pilha final:", pilha)

#--------------------------------------------

palavra = input("Digite uma palavra: ")

pilha = []
# Empilha caracteres
for letra in palavra:
    pilha.append(letra)
# Monta palavra invertida
invertida = ""
while pilha:
    invertida += pilha.pop()
# Verificação
if palavra == invertida:
    print("É palíndromo!")
else:
    print("Não é palíndromo.")

#--------------------------------------------

expressao = input("Digite uma expressão: ")
pilha = []
balanceado = True
for char in expressao:
    if char == "(":
        pilha.append(char)
    elif char == ")":
        if not pilha:
            balanceado = False
            break

pilha.pop()
# Verificação final
if balanceado and not pilha:
    print("Parênteses balanceados!")
else:
    print("Parênteses NÃO estão balanceados.")

#--------------------------------------------


# Estruturas
fila = [] # Fila de clientes (FIFO)
historico = [] # Pilha de atendimentos (LIFO)
while True:
    print("\n===== MENU =====")
    print("1 - Adicionar cliente")
    print("2 - Atender cliente")
    print("3 - Mostrar fila")
    print("4 - Mostrar histórico")
    print("5 - Buscar cliente")
    print("6 - Sair")
opcao = input("Escolha uma opção: ")
# 1 - Adicionar cliente
if opcao == "1":
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cliente = {"nome": nome, "idade": idade}
    fila.append(cliente)
    print("Cliente adicionado à fila!")

# 2 - Atender cliente

elif opcao == "2":
    if not fila:
        print("Fila vazia!")
    else:
        cliente = fila.pop(0)
        print(f"Atendendo: {cliente['nome']} ({cliente['idade']} anos)")
        historico.append(cliente)

# 3 - Mostrar fila
elif opcao == "3":
    if not fila:
        print("Fila vazia!")
    else:
        print("\nFila de atendimento:")
        for c in fila:
            print(f"{c['nome']} ({c['idade']} anos)")
            # 4 - Mostrar histórico (pilha)
elif opcao == "4":
    if not historico:
        print("Nenhum cliente atendido ainda.")
    else:
        print("\nHistórico (último atendido primeiro):")
        for c in reversed(historico):
            print(f"{c['nome']} ({c['idade']} anos)")
    # 5 - Buscar cliente
elif opcao == "5":
    if not fila and not historico:
        print("Nenhum cliente cadastrado.")
    else:
        nome_busca = input("Digite o nome: ")
        encontrado = False

# Busca na fila
for c in fila:
    if c["nome"].lower() == nome_busca.lower():
        print("Cliente está na fila.")
        encontrado = True
# Busca no histórico
for c in historico:
    if c["nome"].lower() == nome_busca.lower():
        print("Cliente já foi atendido.")
        encontrado = True

    if not encontrado:
        print("Cliente não encontrado.")
    # 6 - Sair
    elif opcao == "6":
        print("Encerrando sistema...")
        break

else:
    print("Opção inválida!")