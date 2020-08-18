# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.
# 
# 

a = int(input("Insira um número: "))
b = int(input("Insira outro número: "))

if  a>b:
    print(str(a)+" é o maior")
elif b>a:
    print(str(b)+" é o maior")
else:
    print("Os dois são iguais")
 
