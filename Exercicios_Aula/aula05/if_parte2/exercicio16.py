# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!

def print_comb (tipo_combustivel, litros, desconto):
    print(f'''
                COMBUSTÍVEL: {tipo_combustivel}
                TOTAL ABASTECIDO: {litros_combustivel}l
                DESCONTO:{desconto}%
                ''')

while True:
    try:
        litros_combustivel = float(input('Informe quantos litros de combustível você deseja abastecer: '))
        tipo_combustivel = int(input('''
        1 - Álcool
        2 - Diesel
        3 - Gasolina

        Informe com qual combustível você deseja abastecer: '''))
        if tipo_combustivel == 3:
            if litros_combustivel <= 20:
                print_comb('Gasolina', litros_combustivel, '0')
            else:
                print_comb('Gasolina', litros_combustivel, '10')
        elif tipo_combustivel == 2:
            if litros_combustivel <= 10:
                print_comb('Diesel', litros_combustivel, '1.5')
            else:
                print_comb('Diesel', litros_combustivel, '5')
        elif tipo_combustivel == 1:
            if litros_combustivel <= 10:
                print_comb('Álcool', litros_combustivel, '5')
            else:
               print_comb('Álcool', litros_combustivel, '10')
        else:
                print("Opção Inválida.")
    except:
        print('Oops! Valor inválido. Tente novamente:')
    else:
        x = input('Digite 1 para continuar.')
        if not(x) or not(x == '1'):
            break
