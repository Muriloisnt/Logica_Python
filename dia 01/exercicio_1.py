print("digitenomes (pressione Enter em branco para terinar): ")
nomes = []
while True:
    nome = input("digite o nome: ").strip()
    if nome == "":
        break
    nomes.append(nome)

with open ("nomes.txt", "w", encoding="utf-8") as f:
    for n in nomes:
        f.write(n +"\n")