# =====================================================
#  SIMULADOR DE CAIXA ELETRÔNICO
#  Operações: consultar saldo, sacar, depositar e sair.
#  O saldo de cada conta fica salvo no arquivo saldos.txt
# =====================================================

import os  # usado só para saber se o arquivo já existe

# ---------- CONSTANTES (valores que não mudam) ----------
ARQUIVO = "saldos.txt"                 # arquivo onde os saldos ficam salvos
SALDO_INICIAL = 1000                   # saldo fictício de contas novas
CEDULAS = [100, 50, 20, 10, 5, 2]      # cédulas que o caixa trabalha (da maior p/ menor)


# ---------- FUNÇÕES DE ARQUIVO ----------
def carregar_saldos():
    """Lê o arquivo e devolve um dicionário {conta: saldo}.
    Cada linha do arquivo tem o formato:  conta;saldo"""
    saldos = {}
    if os.path.exists(ARQUIVO):        # se o arquivo ainda não existe, começa vazio
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha != "":
                    conta, saldo = linha.rsplit(";", 1)   # separa pelo último ";"
                    saldos[conta] = int(saldo)
    return saldos


def salvar_saldos(saldos):
    """Grava todas as contas e saldos no arquivo (sobrescreve o conteúdo antigo)."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for conta in saldos:
            arquivo.write(f"{conta};{saldos[conta]}\n")


# ---------- FUNÇÃO DE VALIDAÇÃO ----------
def ler_valor(mensagem):
    """Pede um valor ao usuário e valida.
    Devolve o número inteiro se estiver correto, ou None se houver erro
    (já mostrando a mensagem de erro correspondente)."""
    entrada = input(mensagem).strip()

    # 1) valor fracionário (com ponto ou vírgula)
    if "." in entrada or "," in entrada:
        print("Erro: Valores fracionários não são aceitos. Digite um valor inteiro.")
        return None

    # 2) valor negativo (ex.: -50)
    if entrada.startswith("-") and entrada[1:].isdecimal():
        print("Erro: Valores negativos não são aceitos.")
        return None

    # 3) qualquer coisa que não seja número (letras, vazio, símbolos)
    if not entrada.isdecimal():
        print("Erro: Digite apenas números inteiros.")
        return None

    valor = int(entrada)

    # 4) zero não faz sentido em depósito/saque
    if valor == 0:
        print("Erro: O valor deve ser maior que zero.")
        return None

    return valor


def formatar(valor):
    """Deixa o valor no formato do exemplo: R$ 1250,00"""
    return f"R$ {valor},00"


# ---------- PROGRAMA PRINCIPAL ----------
saldos = carregar_saldos()   # carrega os saldos salvos (se houver)

while True:  # laço externo: volta para a tela de conta e senha após "Sair"
    print("\n" + "=" * 40)
    print("   Bem-vindo ao Caixa Eletrônico!")
    print("=" * 40)
    print("--------- TELA DE LOGIN ---------")
    print("Informe sua conta e senha para iniciar.")
    print("(Neste simulador a senha não é validada.)\n")

    conta = ""
    while conta == "":       # exige que digite alguma conta
        conta = input("Digite sua conta: ").strip()
        if conta == "":
            print("Erro: A conta não pode ficar em branco.")

    senha = ""
    while senha == "":       # exige que digite alguma senha (sem conferir se está certa)
        senha = input("Digite sua senha: ")
        if senha == "":
            print("Erro: A senha não pode ficar em branco.")

    # Se a conta já foi usada, pega o saldo do arquivo. Senão, usa o saldo fictício.
    if conta in saldos:
        saldo = saldos[conta]
        print(f"\nConta {conta} acessada. Saldo carregado do arquivo.")
    else:
        saldo = SALDO_INICIAL
        print(f"\nConta {conta} nova. Saldo inicial de {formatar(SALDO_INICIAL)}.")

    opcao = ""
    while opcao != "4":      # laço do menu: repete até escolher "Sair"
        print(f"\n========== MENU (Conta: {conta}) ==========")
        print("1 - Consultar saldo")
        print("2 - Sacar")
        print("3 - Depositar")
        print("4 - Sair")
        print("==========================")
        opcao = input("Escolha uma opção: ").strip()

        # ----- 1) CONSULTAR SALDO -----
        if opcao == "1":
            print(f"\nSeu saldo atual é: {formatar(saldo)}")
            input("\nPressione ENTER para retornar")

        # ----- 2) SACAR -----
        elif opcao == "2":
            valor = ler_valor("\nDigite o valor para saque: ")
            if valor is not None:                       # só continua se o valor for válido
                if valor > saldo:
                    print("Saldo insuficiente para este saque.")
                else:
                    # Calcula as cédulas ANTES de mexer no saldo
                    restante = valor
                    quantidades = []
                    i = 0
                    while i < len(CEDULAS):
                        quantidades.append(restante // CEDULAS[i])  # quantas cédulas cabem
                        restante = restante % CEDULAS[i]            # o que sobrou
                        i += 1

                    if restante != 0:
                        # sobrou um valor que nenhuma cédula paga (ex.: R$ 1, R$ 11)
                        print("Erro: Este caixa não trabalha com esse valor.")
                        print("Cédulas disponíveis: R$100, R$50, R$20, R$10, R$5 e R$2.")
                    else:
                        saldo = saldo - valor
                        print("Saque realizado com sucesso.")
                        print("Entregar:")
                        i = 0
                        while i < len(CEDULAS):
                            if quantidades[i] > 0:      # só mostra cédulas que serão usadas
                                if quantidades[i] == 1:
                                    print(f"1 cédula de R${CEDULAS[i]}")
                                else:
                                    print(f"{quantidades[i]} cédulas de R${CEDULAS[i]}")
                            i += 1
                        print(f"Saldo atual: {formatar(saldo)}")
            input("\nPressione ENTER para retornar")

        # ----- 3) DEPOSITAR -----
        elif opcao == "3":
            valor = ler_valor("\nDigite o valor para depósito: ")
            if valor is not None:
                saldo = saldo + valor
                print("Depósito realizado com sucesso!")
                print(f"Saldo atual: {formatar(saldo)}")
            input("\nPressione ENTER para retornar")

        # ----- 4) SAIR (salva o saldo no arquivo) -----
        elif opcao == "4":
            saldos[conta] = saldo
            salvar_saldos(saldos)
            print("\nObrigado por usar nosso sistema!")

        # ----- QUALQUER OUTRA COISA = OPÇÃO INVÁLIDA -----
        else:
            print("Opção inválida! Por favor, escolha uma opção de 1 a 4.")