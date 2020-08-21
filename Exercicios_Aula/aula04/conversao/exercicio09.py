
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.


nome = input('Informe seu nome: ')
produto = input('Informe o nome do produto: ')
quantidade = int(input('Informe a quantidade do produto: '))
valor = float(input('Informe o preço do produto: '))

total = quantidade * valor

print(f'Olá, {nome}. Você acaba de comprar {quantidade} unidades do produto {produto}, que custa R$ {valor} a unidade. O valor total da sua compra foi de R$ {total}.')