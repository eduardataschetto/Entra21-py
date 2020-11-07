# Exercicio 3
# 
# Crie 3 variáveis
# 
# Cada variável deve conter um número
# 
# Imprima na tela a soma dos 3 números

while True:
    try:
        a = int(input("Informe um número: "))
        b = int(input("Informe outro número: "))
        c = int(input("Informe um útimo número: "))
        print(a+b+c)
    except ValueError:
        print("Por favor, informe apenas números INTEIROS.")