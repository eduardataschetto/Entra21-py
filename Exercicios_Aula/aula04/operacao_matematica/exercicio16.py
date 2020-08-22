# Exercicio 16
# Foi verificado que a venda de bermudas aumenta conforme aumenta a temperatura (t) (float) conforme a seguinte fórmula:
# 
# bermudas = 1.5t + t + 150
# 
# Lembrando que o t significa temperatura.
# 
# Faça um programa para o seu superior que peça a temperatura e mostre a venda prevista de bermudas.

while True:
    try:
        temperatura = float(input(f'Informe a temperatura(°C): '))
        print(f'''
        A previsão de venda de bermudas é {1.5*temperatura + temperatura + 150}.
        ''')
        break
    except ValueError:
        print('Você informou um valor inválido. Tente novamente.35')