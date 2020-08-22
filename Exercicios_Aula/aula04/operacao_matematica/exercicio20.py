#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

while True:
    try:
        dinheiro_emprestado = float(input("informe o valor emprestado: "))
        taxa_juros = float(input("Informe a taxa de juros: "))
        tempo_emprestimo = int(input("Informe o tempo de empréstimo: "))
    except ValueError:
        print('Valor inválido.Tente Novamente.')
    else:
        valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
        print(f'''O valor emprestado foi de R$ {dinheiro_emprestado}, á uma taxa de juros de {taxa_juros}% a.m. e sob o tempo de empréstimo de {tempo_emprestimo} meses.
        Desse modo, o valor a ser devolvido ao final do empréstimo é de R$ {valor_receber}. ''')
        break