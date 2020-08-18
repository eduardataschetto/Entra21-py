# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

a = int(input("Informe um número: "))
b = int(input("Informe um número: "))
c = int(input("Informe um número: "))

if a<=b and a<=c:
    print(str(a)+" é o menor")
elif b<=a and b<=c:
    print(str(b)+" é o menor")
else:
    print(str(c)+" é o menor")