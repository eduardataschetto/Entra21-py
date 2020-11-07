
"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""
while True:
    media = 0
    for i in range(10):
        nota = float(input(f'Insira sua nota: '))
        media += nota

    media = media / 10

    if media < 5.5:
        print('Reprovado')
    elif media < 7:
        print('Recuperação')
    else:
        print('Aprovado')

    x = input('Digite 1 para continuar: ')
    if not(x == '1') or not(x):
        break