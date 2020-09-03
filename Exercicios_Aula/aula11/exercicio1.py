"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""
op = ''

while op !=  'S':
     op = input(f'''
1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Informe uma opção: ''')

     if op == '1':
         x = float(input('Informe um número: '))
         y = float(input('Informe outro número: '))
         print(f'{x} + {y} = {x+y}')
     elif op == '2':
         x = float(input('Informe um número: '))
         y = float(input('Informe outro número: '))
         print(f'{x} - {y} = {x-y}')
     elif op == '3':
         x = float(input('Informe um número: '))
         y = float(input('Informe outro número: '))
         print(f'{x} x {y} = {x*y}')
     elif op == 'S':
         print('Hasta la vista!! ')
     else:
         print('Opção inálida! ')
