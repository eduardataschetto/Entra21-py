# Exercicio 8
# Faça um programa que peça 3 números inteiros e mostre o número maior.

a = int(input("Informe um número: "))
b = int(input("Informe um número: "))
c = int(input("Informe um número: "))

if a>b:
    if a>c:
        print(str(a)+" é o maior")
    else:
        print(str(c)+" é o maior")
else:
    if b>c:
        print(str(b)+" é o maior")
    else:
        print(str(c)+" é o maior")