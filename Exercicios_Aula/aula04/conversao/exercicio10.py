# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.
class Produtos:
    def __init__ (self, nome, qtde, valor):
        self.nome = nome
        self.qtde = qtde
        self.valor = valor

p = []
num = int(input("informe a quantidade de produtos diferentes desejada: "))
i = int(0)
for i in range(i, num):
    nome = input("Informe o nome do produto:")
    qtde =  input("Informe a quantidade comprada do produto: ")
    valor = input("Informe o valor do produto: ")
    p.append(Produtos (nome, qtde, valor))

for i in p:
    print("Produto 1: "+i.nome+ " Quantidade: "+i.qtde+ " Preço unitário: R$ " +i.valor+ " Preço total: R$ " +str(int(i.qtde)*float(i.valor)))
