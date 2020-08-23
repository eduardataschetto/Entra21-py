# Exercicio 3
# Faça um programa que peça a idade do cliente.
# 
# Se ele tiver 18 anos ou mais deve aparecer a mensagem 'Entrada permitida'
# 
# Caso contrário deve aparecer a mensagem 'Entrada Negada!'

while True:
    try:
        idade = int(input('Informe sua idade: '))
        if idade >= 18:
            print('Entrada permitida')
        else:
            print('Entrada Negada!')
        break
    except ValueError:
        print('Oops! Valor inválido. Tente novamente')