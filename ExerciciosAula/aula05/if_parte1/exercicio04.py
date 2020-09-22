# Exercicio 4
# Escreva um programa que peça a nota de um aluno
# 
# Se a nota for 7 ou mais deve aparecer a mensagem: "Aprovado"
# 
# Caso contrário deve aparecer a mensagem: "Reprovado"

while True:
    try:
        a = float(input('Informe a nota: '))
        if a >= 7:
            print('Aprovado')
        else:
            print('Reprovado')
        break
    except ValueError:
        print('Oops! Valor inválido. Tente novamente:')