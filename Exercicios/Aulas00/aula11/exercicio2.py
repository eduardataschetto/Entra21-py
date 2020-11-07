"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida"
"""
op = ''

while op != 'S':
    op = input('''
A) soma
B) Média
C) Taboada
S) Sair
Informe uma opção:  ''')

    if op == 'A':
        x = float(input('Informe um número: '))
        y = float(input('Informe outro número: '))
        print(f'{x} + {y} = {x + y}')
    elif op == 'B':
        media = 0
        for i in range(4):
            x =  int(input('Informe um número:'))
            media += x
        print(media)
    elif op == 'C':
        x = int(input('Informe um número:'))
        for i in range(11):
            print(f'{x} x {i} = {x*i}' )
    elif op == 'S':
        print('Hasta la vista!!')
    else:
        print('Opção inálida! ')
    
