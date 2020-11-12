def fazer_deposito(numero_conta):
    contas, index = filtrar_conta(numero_conta)
    valor_deposito = int(input("Informe o valor do depósito: R$ "))
    valor = int(contas[index][5])
    contas[index][5] = valor + valor_deposito
    update_contas(contas)
    return True

def filtrar_conta(numero_conta:str) -> list:
    contas = []

    with open("conta.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            conta = linha.split(";")
            contas.append(conta)

        for conta in contas:
            if conta[3] == numero_conta:
                return contas, contas.index(conta)
    f.close()


def update_contas(contas):
    with open("conta.txt", "w") as f:
        for conta in contas:
            f.write(f"{conta[0]};{conta[1]};{conta[2]};{conta[3]};{conta[4]};{conta[5]}\n")
    f.close()
