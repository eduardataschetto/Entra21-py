# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.

a = int(input("Informe a: "))
b = int(input("Informe b: "))
c = int(input("Informe c: "))

delta = (b ** 2) - (4 * a * c)

print("delta = "+str(delta))