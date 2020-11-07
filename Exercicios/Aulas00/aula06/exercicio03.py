# Execicios 03

#Escreva um programa que contenha um menu com 4 opções:
#A) soma
#B) média
#C) divisão
#D) Sair

#As opções podem ser escolhidas com as letras maiusculas ou minusculas.

#Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

#Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

#Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

#Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"

while True:
    try:
        op = input("""
        A) Soma
        B) Média
        C) Divisão
        D) Sair
        Informe a opção desejada: 
        """)

        if op == 'a' or op == 'A':
            a =  float(input("Informe um número: "))
            b =  float(input("Informe um número: "))
            print(str(a+b))
        if op == 'b' or op == 'B':
            a =  float(input("Informe um número: "))
            b =  float(input("Informe um número: "))
            c =  float(input("Informe um número: "))
            d =  float(input("Informe um número: "))
            print(str((a+b+c+d)/4))
        if op == 'c' or op == 'C':
            try:
                a =  float(input("Informe um número: "))
                b =  float(input("Informe um número: "))
                print(+str(a/b))
            except ZeroDivisionError:
                print("Erro! Não pode dividir por ZERO!")
        if op == 'd' or op == 'D':
            print("Muito Obrigado e volte sempre!")
    except ValueError:
        print('Oops! Valor inválido. Tente novamente.')
    else:
        x = input('Informe 1 para continuar . ')
        if not(x == '1') or not(x):
            break
        