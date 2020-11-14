from operacoes import visualizar_saldo, fazer_deposito, saque
from arquivo import valida_login
from getpass import getpass

def acessar_conta():
    while True:
        numero_conta = input("Informe o número da conta: ")
        senha = getpass(prompt = 'Senha:')
        letra = input("Informe a senha de letra: ")
        break
        # if valida_login(numero_conta, senha, letra):
        #     break
        # else:
        #     print("Dados incorretos. Tente novamente.")

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



# acessar_conta()