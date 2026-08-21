linhas = 5

colunas = 10

cinema = []

for i in range(linhas):

    linha = []

    for j in range(colunas):

        linha.append("L") # 'L' para Livre

    cinema.append(linha)

# Pedir ao usuário a linha e a coluna

linha_escolhida = int(input("Digite a linha (0 a 4): "))

coluna_escolhida = int(input("Digite a coluna (0 a 9): "))

# Marcar o assento como ocupado

cinema[linha_escolhida][coluna_escolhida] = "O"

# Exibir o mapa de assentos

print("\nMapa de assentos:")

for linha in cinema:

    for assento in linha:

        print(assento, end=" ")

    print()


linhas = 5

colunas = 10

cinema = []

for i in range(linhas):

    linha = []

    for j in range(colunas):

        linha.append("L") # 'L' para Livre

    cinema.append(linha)

#cinema = [["L" for _ in range(colunas)] for _ in range(linhas)]

def exibir_mapa_e_livres(cinema_mapa):

    print("\nMapa de assentos:")

    assentos_livres = 0

    for linha_mapa in cinema_mapa:

        for assento_mapa in linha_mapa:

            print(assento_mapa, end=" ")

            if assento_mapa == "L":

                assentos_livres += 1

        print()

    print(f"Total de assentos livres: {assentos_livres}")


print("Bem-vindo ao sistema de reserva de assentos do cinema!")

exibir_mapa_e_livres(cinema)

while True:

    try:

        linha_escolhida = int(input(f"\nDigite a linha (0 a {linhas - 1}) para reservar (-1 para sair): "))

        if linha_escolhida == -1:

            break

        coluna_escolhida = int(input(f"Digite a coluna (0 a {colunas - 1}) para reservar: "))

        if not (0 <= linha_escolhida < linhas and 0 <= coluna_escolhida < colunas):

            print("Entrada inválida. Linha ou coluna fora dos limites. Tente novamente.")

            continue

        if cinema[linha_escolhida][coluna_escolhida] == "L":

            cinema[linha_escolhida][coluna_escolhida] = "O" # 'O' para Ocupado

            print(f"Assento na linha {linha_escolhida}, coluna {coluna_escolhida} reservado com sucesso!")

        else:

            print(f"O assento na linha {linha_escolhida}, coluna {coluna_escolhida} já está ocupado.")

        exibir_mapa_e_livres(cinema)

    except ValueError:

        print("Entrada inválida. Por favor, digite um número inteiro.")

    except Exception as e:

        print(f"Ocorreu um erro: {e}")

print("\nObrigado por usar o sistema de reserva de assentos.")