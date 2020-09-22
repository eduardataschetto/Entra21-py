
"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. Depois mostre cada nome em linhas separadas.
"""
nomes = []

for i in range (10):
    nomes.append(input('Informe o nome: '))

for i in nomes:
    print(i)