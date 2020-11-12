from deposito import filtrar_conta, update_contas

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