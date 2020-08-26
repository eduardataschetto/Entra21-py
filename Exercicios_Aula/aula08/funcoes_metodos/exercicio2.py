# 2) Crie uma lista com 10 números qualquer.
# 
# Usando as funções da lista responda:
# 
# Quantos itens tem a lista?
# Qual é o número maior?
# Qual é o número menor?
# Qual é o resultado da soma da lista?
# 
from random import randint

while True:
    list = []
    for i in range(0, 10):
        list.append(randint(0, 30))

    print(list)
    print(f'''
    O maior número da lista é: {max(list)}
    O menor número da lista é: {min(list)}
    O resultado da soma entre os números da lista é: {sum(list)}
    ''')
    x = input('Para continuar digite 1: ')
    if not( x == '1' ) or not(x):
        break
