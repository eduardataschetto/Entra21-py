from operacoes import visualizar_saldo, fazer_deposito, saque, fazer_transferencia
from arquivo import filtrar_conta, limpa_tela
from getpass import getpass

def acessar_conta():
    while True:
        limpa_tela()
        numero_conta = input("Informe o número da conta: ")
        senha = getpass(prompt = 'Senha:' )
        letra =  getpass(prompt = 'Senha de letra: ')
        if valida_login(numero_conta, senha, letra):
            limpa_tela()
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
            limpa_tela()
            visualizar_saldo(numero_conta)
        elif option == 2:
            limpa_tela()
            fazer_deposito(numero_conta)
        elif option == 3:
            limpa_tela()
            saque(numero_conta)
        elif option == 4:
            limpa_tela()
            fazer_transferencia(numero_conta)
        # elif option == 5:
        #     contar()
        #     visualizar_dados(numero_conta, quant)
        else:
            break


def valida_login(numero_conta, senha, letra):
    contas, index = filtrar_conta(numero_conta)
    if contas:
        if senha == contas[index][4] and letra.upper() == contas[index][8]:
            return True
    return False
