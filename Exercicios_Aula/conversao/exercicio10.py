# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

nome1 = input("Informe o nome do produto 1:")
prod1 = int(input("Informe a quantidade comprada do produto 1: "))
valor1 = float(input("Informe o valor do produto 1: "))

nome2 = input("Informe o nome do produto 2:")
prod2 = int(input("Informe a quantidade comprada do produto 2: "))
valor2 = float(input("Informe o valor do produto 2: "))

print("Produto 1: "+nome1+ " Quantidade: "+str(prod1)+ " Preço unitário: R$ " +str(valor1)+ " Preço total: R$ " +str(prod1*valor1))
print("Produto 2: "+nome2+ " Quantidade: "+str(prod2)+ " Preço unitário: R$ " +str(valor2)+ " Preço total: R$ " +str(prod2*valor2))