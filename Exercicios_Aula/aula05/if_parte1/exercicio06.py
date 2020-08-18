# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

a = int(input("Insira um número: "))
b = int(input("Insira outro número: "))

if  a>b:
    print(str(b)+" "+str(a))
elif b>a:
    print(str(a)+" "+str(b))
