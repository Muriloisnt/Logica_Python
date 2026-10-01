import os

ARQUIVO = "saldos.txt"


def limpar_tela():
    os.system("cls")


contas = {}

if os.path.exists(ARQUIVO):

    arquivo = open(ARQUIVO, "r")

    for linha in arquivo:

        conta, saldo = linha.strip().split(";")
        contas[conta] = int(saldo)

    arquivo.close()


while True:
    limpar_tela()

    print("Bem-vindo ao Caixa Eletrônico!")
    print()

    conta = input("Digite sua conta: ")
    senha = input("Digite sua senha: ")

    if conta in contas:
        saldo = contas[conta]
    else:
        saldo = 1000

    while True:

        limpar_tela()

        print("MENU")
        print("1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            print()
            print("Seu saldo atual é: R$", saldo)
            input("\nPressione ENTER para retornar")


        elif opcao == "2":

            valor = input("\nDigite o valor para saque: ")

            if "." in valor or "," in valor:

                print("Erro: Valores fracionários não são aceitos.")

            elif not valor.isdigit():

                print("Erro: Digite apenas números.")

            else:

                valor = int(valor)

                if valor <= 0:

                    print("Erro: O valor deve ser maior que zero.")

                elif valor > saldo:

                    print("Erro: Saldo insuficiente.")

                else:

                    restante = valor

                    for cedula in [100, 50, 20, 10, 5, 2]:

                        quantidade = restante // cedula

                        if quantidade > 0:

                            print(
                                quantidade,
                                "cédula(s) de R$",
                                cedula
                            )

                        restante = restante % cedula


                    if restante != 0:

                        print(
                            "Erro: O caixa não consegue "
                            "formar esse valor."
                        )

                    else:

                        saldo = saldo - valor

                        print("\nSaque realizado com sucesso.")
                        print("Saldo atual: R$", saldo)

            input("\nPressione ENTER para retornar")


        elif opcao == "3":

            valor = input("\nDigite o valor para depósito: ")

            if "." in valor or "," in valor:

                print("Erro: Valores fracionários não são aceitos.")

            elif not valor.isdigit():

                print("Erro: Digite apenas números.")

            else:

                valor = int(valor)

                if valor <= 0:

                    print("Erro: O valor deve ser maior que zero.")

                else:

                    saldo = saldo + valor

                    print("\nDepósito realizado com sucesso!")
                    print("Saldo atual: R$", saldo)

            input("\nPressione ENTER para retornar")


        elif opcao == "4":

            contas[conta] = saldo

            arquivo = open(ARQUIVO, "w")

            for conta_salva in contas:

                arquivo.write(
                    conta_salva + ";" +
                    str(contas[conta]) + "\n"
                )

            arquivo.close()

            print("\nObrigado por usar nosso sistema!")

            input("\nPressione ENTER para retornar")

            break


        else:

            print("\nOpção inválida!")

            input("\nPressione ENTER para retornar")
