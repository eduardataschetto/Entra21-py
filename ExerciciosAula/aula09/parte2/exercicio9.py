
"""Exercicio 09

Faça um programa que pegue uma lista de valores e separe em 2 listas. Uma com valores menores que 500.00 e outra com maiores ou igual.

Depois motre o maior e o menor valor da cada lista.

vandas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
"""
vendas = [100.00, 500.00, 258.50, 710.00, 50.50,750.00, 10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00, 950.00, 89.90, 2500.00, 1750.00,500.00]
menor = []
maior = []

for i in vendas:
    if i >= 550:
        maior.append(i)
    else:
        menor.append(i)

print(f'''O maior e o menor valor da lista de vendas menores são R$ {maior(menor)} e R$ {menor(menor)}, respectivamente.
Em relação a lista das vendas maiores, temos que R${maior(maior)} e R$ {menor(menor)} são o maior e o menor valor.''')