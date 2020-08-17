
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

nome = input("Informe seu nome: ")
qtde = int(input("Informe a quantidade do produto: "))
valor = float(input("Informe o preço do produto: "))
total = qtde*valor
print("Olá, " +nome+ ". O valor total da venda é R$ " +str(total))