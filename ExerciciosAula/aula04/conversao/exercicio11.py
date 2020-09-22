# Exercicio 11
# Escreva um programa que peça o peso (float) de 3 pessoas e motre na tela a soma de todos os pesos. 

while True:
    try:
        peso1 = float(input('Informe o peso 1: '))
        peso2 = float(input('Informe o peso 2: '))
        peso3 = float(input('Informe o peso 3: '))
        print(f'A soma dos pesos {peso1}Kg, {peso2}Kg e {peso3}Kg é igual a {(peso1+peso2+peso3)}Kg.')
        break
    except ValueError:
        print('Você informou um valor inválido. Tente novamente.')




