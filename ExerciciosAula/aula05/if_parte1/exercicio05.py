# Exercicio 5
# Faça um programa que peça uma senha ao usuário.
# 
# Se a senha for igual a "Abacaxi" deve aparecer a mensagem "Entrada liberada"
# 
# Caso contrário deve aparecer a mensagem "Senha incorreta"
import getpass

while True:
    try:
        password = getpass.getpass('Informe a senha: ')
        if password == 'Abacaxi':
            print('Entrada liberada')
            break
        else:
            print('Senha incorreta')
    except ValueError as e:
        print('Oops! Tente novamente: ')