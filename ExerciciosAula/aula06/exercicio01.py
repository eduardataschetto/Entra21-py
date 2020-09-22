# Execicios 01
# Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições
# Venda Total
# de R$ 0.00 a R$ 30000.00 - 0%
# de R$ 30000.01 a R$ 50000.00 - 1.5%
# de R$ 50000.01 a R$ 100000.00 - 2.5%
# Acima de R$ 100000.00 - 3.5%

while True:
    try:
        venda_total = float(input('Informe a venda total: '))
        if venda_total <= 30000:
            porcentagem_comissao = 0
        elif venda_total >= 30000.01 and venda_total <= 50000:
            porcentagem_comissao = 1.5
        elif venda_total  >= 50000.01 and venda_total <= 100000:
            porcentagem_comissao = 2.5
        else:
            porcentagem_comissao = 3.5
        comissao_total = venda_total * (porcentagem_comissao/100)
        print(f'''
        Venda total: {venda_total}
        Porcentagem de comissão: {porcentagem_comissao}%
        Comissão total: {comissao_total}
        ''')
    except ValueError:
        print('Oops! Valor inválido. Tente novamente.')
    else:
        x = input('Digite 1 para continuar:')
        if not(x) or not(x == '1'):
            break