# Exercicio 15
# Crie um programa que solicite o valor de x (inteiro)
# 
# calcule usando a fórmula 3x-x+3
# 
# mostre o resultado
while True:
    try:
        x = int(input('Informe um número inteiro para calcular o resultado da equação  3x-x+3:  '))
        print(f'O resultado da equação 3 x {x} - {x}+ 3 é { 3*x-x+3}.')
        break
    except ValueError:
        print('Por favor, digite apenas números INTEIROS. Tente novamente: ')