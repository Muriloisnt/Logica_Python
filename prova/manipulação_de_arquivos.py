# MANIPULAÇÃO DE ARQUIVOS EM PYTHON

# Arquivos armazenam dados de forma permanente.
# Podem guardar textos, números, configurações, registros etc.

# TIPOS DE ARQUIVOS

# Arquivos de texto:
# .txt, .csv, .json

# Arquivos binários:
# .jpg, .exe, .mp3


# FUNÇÃO open()

# Sintaxe:
# open(nome_arquivo, modo)

# Exemplo:
arquivo = open("dados.txt", "r")

# Leitura:
conteudo = arquivo.read()

print(conteudo)

# Fechamento:
arquivo.close()


# USANDO with

# O with abre e fecha o arquivo automaticamente.
# É a forma recomendada para trabalhar com arquivos.

with open("dados.txt", "r") as f:
    conteudo = f.read()

print(conteudo)


# MODOS DE ABERTURA

# "r"  = leitura
# "w"  = escrita
# "a"  = adiciona conteúdo no final
# "r+" = leitura e escrita
# "w+" = escrita e leitura, apaga o conteúdo anterior
# "a+" = leitura e escrita, adiciona no final
# "x"  = cria um novo arquivo, gera erro se já existir


# LEITURA DE ARQUIVOS

# read()
# Lê todo o conteúdo do arquivo.

with open("exemplo.txt", "r") as f:
    conteudo = f.read()

print(conteudo)


# readline()
# Lê uma linha por vez.

with open("exemplo.txt", "r") as f:
    linha1 = f.readline()
    linha2 = f.readline()

print(linha1)
print(linha2)


# readlines()
# Lê todas as linhas e retorna uma lista.

with open("exemplo.txt", "r") as f:
    linhas = f.readlines()

for linha in linhas:
    print(linha.strip())


# LENDO LINHA POR LINHA COM for

with open("exemplo.txt", "r") as f:
    for linha in f:
        print(linha)


# seek(0)
# Volta o cursor para o início do arquivo.

with open("exemplo.txt", "r") as f:
    conteudo = f.read()

    f.seek(0)

    conteudo_novamente = f.read()

print(conteudo_novamente)


# ESCRITA DE ARQUIVOS

# write()
# Escreve uma string no arquivo.
# Não adiciona quebra de linha automaticamente.

with open("saida.txt", "w") as f:
    f.write("Ola, mundo!\n")
    f.write("Segunda linha.\n")


# writelines()
# Escreve várias strings de uma vez.
# Também não adiciona \n automaticamente.

linhas = [
    "Linha 1\n",
    "Linha 2\n",
    "Linha 3\n"
]

with open("saida.txt", "w") as f:
    f.writelines(linhas)


# EXEMPLO COMPLETO

nomes = ["Ana", "Bruno", "Carlos"]

with open("nomes.txt", "w") as f:
    for nome in nomes:
        f.write(nome + "\n")


# ADICIONANDO CONTEÚDO SEM APAGAR O ANTERIOR

with open("nomes.txt", "a") as f:
    f.write("Maria\n")


# LENDO O ARQUIVO

with open("nomes.txt", "r") as f:
    for linha in f:
        print(linha.strip())


# ESCREVENDO NÚMEROS

# write() aceita strings.
# Para escrever números, use str().

idade = 20

with open("dados.txt", "w") as f:
    f.write(str(idade))


# RESUMO

# r  -> ler
# w  -> escrever e apagar o conteúdo anterior
# a  -> adicionar no final
# x  -> criar arquivo novo

# read()      -> lê tudo
# readline()  -> lê uma linha
# readlines() -> retorna todas as linhas em uma lista
# write()     -> escreve uma string
# writelines() -> escreve várias strings
# seek(0)     -> volta para o início

# Boa prática:
# Sempre que possível, use:

with open("arquivo.txt", "r") as f:
    conteudo = f.read()