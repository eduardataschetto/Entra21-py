# Exercicio 8
# Faça um programa que peça 3 números inteiros e mostre o número maior.

while True:
    try:
        a = int(input('Informe um número: '))
        b = int(input('Informe um número: '))
        c = int(input('Informe um número: '))
        if a > b:
            if a > c:
                print(f'{a} é o maior')
            else:
                print(f'{c} é o maior')
        else:
            if b > c:
                print(f'{b} é o maior')
            else:
                print(f'{c} é o maior')
        break
    except ValueError:
        print('Valor inválido. Tente novamente: ')