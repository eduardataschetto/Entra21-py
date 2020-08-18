# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
# 

a = int(input("Informe um número: "))
b = int(input("Informe um número: "))
c = int(input("Informe um número: "))

l = [a, b, c]

print(sorted(l, reverse = True))
