def quadrado():
    # Primeira parte
    print('+', end='')
    for c in range(2, 20):
        print('-', end='')
    print('+')

    # Segunda parte
    for l in range(2, 5):
        print('|', end='')
        for c in range(2, 20):
            print(' ', end='')
        print('|')

    # Terceira parte
    print('+', end='')
    for c in range(2, 20):
        print('-', end='')
    print('+')

# Chamando a função para executar tudo
quadrado()




