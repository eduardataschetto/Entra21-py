from operacoes import visualizar_saldo, fazer_deposito, saque
from arquivo import filtrar_conta
from getpass import getpass

def acessar_conta():
    while True:
        numero_conta = input("Informe o número da conta: ")
        senha = getpass(prompt = 'Senha:' )
        letra =  getpass(prompt = 'Senha de letra: ')
        if valida_login(numero_conta, senha, letra):
            print("Dados corretos")
            break
        else:
            print("Dados incorretos. Tente novamente.")

    while True:
        option = int(input(f'''
        1 - Visualizar Saldo
        2 - Fazer um depósito
        3 - Saque
        4 - Transferência
        5 - Visualizar Dados
        6 - Sair\n\nR: '''))

        if option == 1:
            visualizar_saldo(numero_conta)
        elif option == 2:
            fazer_deposito(numero_conta)
        elif option == 3:
            saque(numero_conta)
        elif option == 4:
            pass
            #fazer_transferencia(numero_conta)
        # elif option == 5:
        #     contar()
        #     visualizar_dados(numero_conta, quant)
        else:
            break


def valida_login(numero_conta, senha, letra):
    contas, index = filtrar_conta(numero_conta)
    if senha == contas[index][4] and letra == contas[index][8]:
        print(contas[index])
        return True
    return False
    print(contas[index])



acessar_conta()