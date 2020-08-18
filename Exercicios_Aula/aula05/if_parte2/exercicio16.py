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
# 

litros = float(input("Informe quantos litros você deseja abastecer: "))

tipo_comb = input("""
Informe qual combustível você deseja:
1 - Álcool
2 - Diesel
3 - Gasolina
""")

if tipo_comb == '3':
    if litros <= 20:
        print("Combustível: GASOLINA \nTotal Abastecido: "+str(litros)+"\nDesconto: 0%")
    else:
        print("Combustível: GASOLINA \nTotal Abastecido: "+str(litros)+"\nDesconto: 10%")
elif tipo_comb == '2':
    if litros <= 10:
        print("Combustível:  DIESEL \nTotal Abastecido: "+str(litros)+"\nDesconto: 1.5%")
    else:
        print("Combustível: DIESEL \nTotal Abastecido: "+str(litros)+"\nDesconto: 5%")
elif tipo_comb == '1':
    if litros <= 10:
        print("Combustível:  ÁLCOOL \nTotal Abastecido: "+str(litros)+"\nDesconto: 5%")
else:
        print("Opção Inválida")
