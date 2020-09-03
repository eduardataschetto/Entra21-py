"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""

vendas_dia = []
cont = int(input('Quantas vendas você fez hoje? '))

for i in range(1, (cont + 1)):
    vendas_dia.append(float(input(f'Informe a venda {i}: ')))

print(f'Média de vendas: R$ {sum(vendas_dia) / cont } \nTotal de vendas: R$ {sum(vendas_dia)}')