# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.
# 
# 
while True:
    try:
        a = int(input('Insira um número: '))
        b = int(input('Insira outro número: '))
        if  a>b:
            print(f'{a} é o maior')
        elif b>a:
            print(f'{b} é o maior')
        else:
            print('Os dois são iguais')
    except ValueError:
        print('Oops! Valor inválido! Tente novamente.')
    else:
        x = input('Para continuar digite 1 e para sair digite 0: ')
        if  not(x == 1):
            break
