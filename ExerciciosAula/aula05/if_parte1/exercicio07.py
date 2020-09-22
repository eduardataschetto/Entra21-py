# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

while True:
    try:
        a = int(input('Informe um número: '))
        b = int(input('Informe um número: '))
        c = int(input('Informe um número: '))
        if a <= b and a <= c:
            print(f'{a}é o menor')
        elif b <= a and b <= c:
            print(f'{b}é o menor')
        else:
            print(f'{c}é o menor')
        break
    except ValueError:
        print('Oops! Valor inválido. Tente novamente: ')