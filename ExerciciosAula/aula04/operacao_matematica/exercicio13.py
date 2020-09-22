# Exercicio 13
# Crie um programa que solicite o valor de x (inteiro)
# 
# calcule usando a fórmula x+3
# 
# mostre o resultado

while True:
    try:
        x = int(input('Informe um número inteiro para a soma: '))
        print(f'O resultado da soma {x} + 3 é {x+3}.')
        break
    except ValueError:
        print('Por favor, digite apenas números INTEIROS. Tente novamente: ')