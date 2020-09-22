# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

while True:
    try:
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        if  a>b:
            print(f'{b}, {a}')
        elif b>a:
            print(f'{a}, {b}')
        break
    except ValueError:
        print('Oops! Valor inválido. Tente novamente: ')
