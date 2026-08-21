def imprime_nome(nome) :
    print('Nome:', nome)
    # sem return explicito

resultado = imprime_nome('Ana')
print(resultado)

# Saida:
# nome: Ana
# None





# Criação do tabuleiro 3x3

tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

# Função para exibir o tabuleiro

def mostrar_tabuleiro():

    print("\nTabuleiro:\n\n")

    for i in range(3):

        print(" | ".join(tabuleiro[i]))

        if i < 2:

            print("_" * 9)

    print()

# Função para verificar vitória

def verificar_vitoria(jogador):

    # Linhas

    for linha in tabuleiro:

        if all(celula == jogador for celula in linha):

            return True

    # Colunas

    for col in range(3):

        if all(tabuleiro[lin][col] == jogador for lin in range(3)):

            return True

    # Diagonais

    if all(tabuleiro[i][i] == jogador for i in range(3)):

        return True

    if all(tabuleiro[i][2 - i] == jogador for i in range(3)):

        return True

    return False

# Função principal do jogo

def jogar():

    jogador_atual = "X"

    jogadas = 0

    while True:

        mostrar_tabuleiro()

        print(f"Jogador {jogador_atual}")

        linha = int(input("Informe a linha (0-2): "))

        coluna = int(input("Informe a coluna (0-2): "))

        # Verifica se a posição está livre

        if tabuleiro[linha][coluna] != " ":

            print("Posição ocupada! Tente novamente.")

            continue

        # Faz a jogada

        tabuleiro[linha][coluna] = jogador_atual

        jogadas += 1

        # Verifica vitória

        if verificar_vitoria(jogador_atual):

            mostrar_tabuleiro()

            print(f"O jogador {jogador_atual} venceu!")

            break

        # Verifica empate

        if jogadas == 9:

            mostrar_tabuleiro()

            print("Houve empate!")

            break

        # Alterna jogador

        jogador_atual = "O" if jogador_atual == "X" else "X"

################

# Inicia o jogo

jogar()