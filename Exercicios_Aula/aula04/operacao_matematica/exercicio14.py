
# Exercicio 14
# Crie um programa que solicite o valor de x (inteiro)
# 
# calcule usando a fórmula 2x+3
# 
# mostre o resultado

while True:
    try:
        x = int(input('Informe um número inteiro para calcular o resultado da equação  2x+3:  '))
        print(f'O resultado da equação 2 x {x} + 3 é {2*x+3}.')
        break
    except ValueError:
        print('Por favor, digite apenas números INTEIROS. Tente novamente: ')