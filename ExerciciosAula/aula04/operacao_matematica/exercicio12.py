# Exercicio 12
# 
# Crie um program que peça ao usuário que digite 2 números reais(float) e mostre:
# 
# A soma dos dois
# A multiplicação dos dois
# A divisão do primeiro com o segundo
# A subtração dos dois

while True:
    try:
        n1 = float(input('Informe um número real: '))
        n2 = float(input('Informe outro número real: '))
    except ValueError:
        print('Você informou um valor inválido. Tente novamente.')
    else:
        print(f'''
        {n1} + {n2} = {n1+n2}
        {n1} x {n2} = {n1*n2}
        {n1} / {n2} = {n1/n2}
        {n1} - {n2} = {n1-n2}
        ''')
        break
        