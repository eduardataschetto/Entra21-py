from arquivo import filtrar_conta, update_contas, filtrar_pessoa

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
    print('Saldo insuficiente')


def visualizar_saldo(numero_conta):
    file = open("conta.txt", "r")
    for procura in file: 
        linha = procura.strip()
        lista_conta = linha.split(";")
        if numero_conta == lista_conta[3]:
            print(f"Seu saldo é: {lista_conta[5]}")
            return int(lista_conta[5])
    file.close()


def fazer_transferencia(numero_conta):
    while True:
        numconta_transferencia = input("Informe o número da conta para fazer transferência: ")
        lista, index = filtrar_conta(numconta_transferencia)
        pessoa = filtrar_pessoa(lista[index][1])
        valor = 0

        valida_transferencia = 0
        while True:
            try:
                valida_transferencia = int(input(f"TRANSFERIR PARA:  {pessoa[1]}\nNÚMERO DA CONTA: {numconta_transferencia}\n1 - SIM\t2 - NÃO\nInforme: "))
                if valida_transferencia in [1, 2]:
                    break
            except ValueError:
                print("Opção Inválida!")

        if valida_transferencia == 1:
            while True:
                saldo = visualizar_saldo(numero_conta)
                valor = int(input("Informe o valor que você deseja transferir: "))
                if valor > saldo:
                    print("Ops! Você possui um saldo inferior ao valor que deseja transferir! Insira outro valor: ")
                else:
                    break
        else:
            continue
            
        valida_valor = 0
        while True:
            try:
                valida_valor = int(input(f"TRANSFERIR R$ {valor:.2f} PARA:  {pessoa[1]}\nNÚMERO DA CONTA: {numconta_transferencia}\n1 - SIM\t2 - CANCELAR\nInforme: "))
                if valida_valor in [1, 2]:
                    break
            except ValueError:
                print("Opção Inválida!")

        if valida_valor == 1:
            lista[index][5] = int(lista[index][5]) + valor
            update_contas(lista)
            print(f"Você transferiu R$ {valor:.2f} para {pessoa[1]}")
            break
        else:
            break