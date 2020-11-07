
"""Exercicio 02

Faça um programa que mostre a tabuada de 1, 2, 3 e 4
"""
for i in range(1, 5):
    print(f'TABUADA DO {i}')
    for j in range(1, 11):
        print(f' {i} x {j} = {i * j}')
    print('\n')