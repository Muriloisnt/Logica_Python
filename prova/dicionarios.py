#Exemplo Completo: Atualização e Inserção
tabela = {
"Alface": 0.45,
"Batata": 1.20,
"Tomate": 2.30,
"Feijão": 1.50
}
tabela["Tomate"] = 2.50 # Atualiza valor existente
tabela["Cebola"] = 1.20 # Adiciona nova chave
print(tabela)

#Observe que "Tomate" teve seu preço alterado e "Cebola" foi inserida ao final, mantendo a ordem de inserção.
#---------------------------------------------
#O operador in retorna True ou False, permitindo verificar a existência de uma chave de forma segura antes do acesso.

tabela = {
"Alface": 0.45,
"Batata": 1.20,
"Tomate": 2.30,
"Feijão": 1.50
}
print("Batata" in tabela) # True
print("Manga" in tabela) # False
#---------------------------------------------
#Apagando Chaves com del

#A instrução del remove uma chave e seu valor do dicionário. Se a chave não existir, ocorre um erro KeyError.

tabela = {"Alface":0.45, "Batata":1.20, "Tomate":2.30, "Feijão":1.50}
print(tabela)
del tabela["Alface"]
print(tabela)
#---------------------------------------------
#Acessando Chaves e Valores

#Os métodos keys() e values() retornam geradores — objetos que produzem os itens sob demanda. Use-os
#diretamente em loops ou converta com list().

tabela = {"Alface":0.45, "Batata":1.20, "Tomate":2.30}
print(tabela.keys()) # dict_keys(['Alface', 'Batata'])
print(tabela.values()) # dict_values([0.45, 1.20])
print(list(tabela.keys())) # converte para lista

#keys()Retorna todas as chaves dodicionário

#values()Retorna todos os valores armazenados

#list()Converte o gerador em uma lista navegável

#---------------------------------------------

#Iterando com items()

#O método items() retorna os pares chave-valor, permitindo percorrer o dicionário de forma elegante com for.

tabela = {"Alface":0.45, "Batata":1.20, "Tomate":2.30, "Feijão":1.50}
for chave, valor in tabela.items():
    print(chave, "->", valor)

#---------------------------------------------

#Dicionários com Listas como Valores
estoque = {
"Alface": [10, 0.45],
"Batata": [5, 1.20],
"Tomate": [8, 2.30],
"Feijão": [3, 1.50]
}
# chave: nome do produto
# valor: [quantidade, preço]

#---------------------------------------------
# Acessando e Atualizando o Estoque
estoque = {"Alface": [10, 0.45], "Batata": [5, 1.20]}
# Ler quantidade e preço
qtd = estoque["Alface"][0] # 10
preco = estoque["Alface"][1] # 0.45
# Atualizar após uma venda
estoque["Alface"][0] -= 2 # agora tem 8 unidades
# Atualizar preço
estoque["Batata"][1] = 1.35


#---------------------------------------------
# Criando o dicionário vazio
alunos = {}
# Cadastro de 3 alunos
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota
# Exibindo os dados
print("\nLista de alunos:")
soma = 0
for nome, nota in alunos.items():
    print(f"Aluno: {nome} - Nota: {nota}")
    soma += nota
# Calculando média
media = soma / len(alunos)
print(f"\nMédia da turma: {media:.2f}")

#---------------------------------------------
# Dicionário de produtos

tabela = {
"Alface": 0.45,
"Batata": 1.20,
"Tomate": 2.30,
"Feijão": 1.50
}
# Entrada do usuário
produto = input("Digite o nome do produto: ")
# Verificando se existe
if produto in tabela:
    print(f"Preço: R$ {tabela[produto]:.2f}")
else:
    print("Produto não encontrado.")

#---------------------------------------------

frase = input("Digite uma frase: ")

# Separando as palavras
palavras = frase.split()
# Dicionário para contagem
contador = {}
# Contando as palavras
for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
else:
    contador[palavra] = 1

# Exibindo resultado
print("\nContagem de palavras:")
for palavra, quantidade in contador.items():
    print(f"{palavra}: {quantidade}")
