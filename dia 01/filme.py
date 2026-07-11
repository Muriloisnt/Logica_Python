import os


def carregar_filmes():
    filmes = []
    filme_atual = {}

    # Define o nome do arquivo
    nome_arquivo = "arquivo_filme.txt"

    # Se o arquivo não existir, exibe um aviso claro e retorna uma lista vazia
    if not os.path.exists(nome_arquivo):
        print(f"\n[AVISO]: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Certifique-se de que ele está na mesma pasta do seu script!")
        return []

    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                # Linha vazia indica fim do bloco de um filme
                if not linha:
                    if filme_atual:
                        filmes.append(filme_atual)
                        filme_atual = {}
                    continue

                if ":" in linha:
                    chave, valor = linha.split(":", 1)
                    chave = chave.strip().lower()
                    valor = valor.strip()

                    if "titulo" in chave:
                        filme_atual["titulo"] = valor
                    elif "diretor" in chave:
                        filme_atual["diretor"] = valor
                    elif "geero" in chave or "genero" in chave:
                        # Divide gêneros por vírgula e remove espaços extras
                        filme_atual["generos"] = [
                            g.strip().lower() for g in valor.split(",")
                        ]
                    elif "duracao" in chave:
                        # Filtra apenas os dígitos numéricos (remove "minutos", "min", etc.)
                        apenas_numeros = "".join(
                            char for char in valor if char.isdigit()
                        )
                        filme_atual["duracao"] = (
                            int(apenas_numeros) if apenas_numeros else 0
                        )

            # Adiciona o último filme caso o arquivo acabe sem linha vazia
            if filme_atual:
                filmes.append(filme_atual)

    except Exception as e:
        print(f"\n[ERRO AO LER ARQUIVO]: {e}")

    return list(filmes)


def menu():
    print("\n" + "=" * 35)
    print("      CONTAGEM DO ARQUIVO      ")
    print("=" * 35)
    print("1 - Contar Total de Filmes")
    print("2 - Contar Filmes por Diretor")
    print("3 - Contar Filmes por Gênero")
    print("4 - Média de Duração")
    print("5 - Sair")
    print("=" * 35)


def contar_total(lista):
    print(f"\n-> Total de filmes no arquivo: {len(lista)}")


def contar_por_diretor(lista):
    print("\n--- QUANTIDADE POR DIRETOR ---")
    if not lista:
        print("Nenhum filme carregado para contar.")
        return

    contagem = {}
    for filme in lista:
        diretor = filme.get("diretor", "Desconhecido").title()
        contagem[diretor] = contagem.get(diretor, 0) + 1

    for diretor, qtd in contagem.items():
        print(f"Diretor: {diretor} -> {qtd} filme(s)")


def contar_por_genero(lista):
    print("\n--- QUANTIDADE POR GÊNERO ---")
    if not lista:
        print("Nenhum filme carregado para contar.")
        return

    contagem = {}
    for filme in lista:
        for genero in filme.get("generos", []):
            genero_formatado = genero.title()
            contagem[genero_formatado] = contagem.get(genero_formatado, 0) + 1

    for genero, qtd in contagem.items():
        print(f"Gênero: {genero} -> {qtd} filme(s)")


def media_duracao(lista):
    print("\n--- MÉDIA DE DURAÇÃO ---")
    if not lista:
        print("Nenhum filme carregado para calcular a média.")
        return

    total_minutos = sum(filme.get("duracao", 0) for filme in lista)
    media = total_minutos / len(lista)
    print(f"A média de duração geral é de {media:.1f} minutos")


if __name__ == "__main__":
    while True:
        menu()
        opc = input("Escolha uma opção: ").strip()

        # Recarrega o arquivo sempre que uma opção é selecionada para pegar atualizações
        lista_de_filmes = carregar_filmes()

        if opc == "1":
            contar_total(lista_de_filmes)
        elif opc == "2":
            contar_por_diretor(lista_de_filmes)
        elif opc == "3":
            contar_por_genero(lista_de_filmes)
        elif opc == "4":
            media_duracao(lista_de_filmes)
        elif opc == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Digite de 1 a 5.")
