# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

a = float(input("Informe um número: "))

if a > 0:
    print("POSITIVO")
elif a < 0:
    print("NEGATIVO")
else:
    print("NÚMERO NULO")