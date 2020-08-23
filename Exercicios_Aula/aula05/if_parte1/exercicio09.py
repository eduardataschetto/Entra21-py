# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.

while True:
    try:
            a = int(input('Informe um número: '))
            b = int(input('Informe um número: '))
            c = int(input('Informe um número: '))
            if a > b:
                aux = a
                a = b
                b = aux
            if a > c:
                aux = a 
                a = c
                c = aux
            if b > c:
                aux = b
                b = c
                c = aux
            print(f'{a}, {b}, {c}')
            break
    except:
        print('Oops! Valor inválido. Tente novamente: ')

