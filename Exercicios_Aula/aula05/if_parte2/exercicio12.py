# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

a = float(input("Informe um número: "))
b = float(input("Informe um número: "))

op = input("""
#######################
OPERAÇÕES
1 - ADIÇÃO
2 - SUBTRAÇÃO
3 - DIVISÃO
4 - EXPOENENCIAÇÃO
########################
Informe a opção desejada:
""")

if op == '1':
    print(str(a+b))
elif op == '2':
    print(str(a-b))
elif op == '3':
    print(str(a/b))
elif op == '4':
    print(str(a**b))
else:
    print("Opção Inválida")

