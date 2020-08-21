# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.
class Produtos:
    def __init__ (self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

p = []
num = int(input("informe a quantidade de produtos diferentes que você deseja informar: "))
for i in range(0, num):
    nome_produto = input("Informe o nome do produto: ")
    quantidade_produto =  input("Informe a quantidade comprada do produto: ")
    valor_produto= input("Informe o valor do produto: ")
    print('\n')
    p.append(Produtos (nome_produto, quantidade_produto, valor_produto))

for i in p:
    print(f'''
    Nome: {i.nome}
    Quantidade: {i.quantidade}
    Valor Unitário: {i.valor}
    Valor Total: {int(i.quantidade)*float(i.valor)}
    ''')
