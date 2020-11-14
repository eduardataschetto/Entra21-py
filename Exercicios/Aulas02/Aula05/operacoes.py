from arquivo import filtrar_conta, update_contas

def fazer_deposito(numero_conta):
    contas, index = filtrar_conta(numero_conta)
    valor_deposito = int(input("Informe o valor do depósito: R$ "))
    valor = int(contas[index][5])
    contas[index][5] = valor + valor_deposito
    update_contas(contas)
    return True


def saque(numero_conta):
    lista_contas, index = filtrar_conta(numero_conta)
    saldo = int(lista_contas[index][5])
    print(f'Saldo atual: {saldo}')

    if saldo > 0:
        valor = int(input('Valor do saque: '))
        if saldo >= valor:
            saldo = saldo - valor
            lista_contas[index][5] = saldo
            update_contas(lista_contas)
            print('Saque realizado!')
            return True
    else:
        print('Saldo insuficiente')
        return False


def visualizar_saldo(numero_conta):
    file = open("conta.txt", "r")
    for procura in file: 
        linha = procura.strip()
        lista_conta = linha.split(";")
        if numero_conta == lista_conta[3]:
            print(f"Seu saldo é: {lista_conta[5]}")
    file.close()