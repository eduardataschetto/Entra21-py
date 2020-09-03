"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Psicina de bolinhas liberado
"""

for i in range(10):
    idade = int(input('Informe a idade: '))
    if idade < 13:
        print('Psicina de bolinhas liberado! ')
    elif idade < 16:
        print('Ingreços para fliperama liberado!')
    elif idade < 18:
        print('Ingreços de cinema liberado!')
    else:
        print('Ingreços da Rave liberado!')
