# Execicios 02

#Escreva um programa que receba 4 notas e calcule a média.
#Mostre a seguinte mensagem conforme a media final.

#Media Final
#de 0 a 5 - Reprovado
#de 5 a 6.5 - Recuperação
#de 6.5 a 9 - Aprovado
#Acima de 9 - Aprovado com louvor

n1 = float(input("Informe a nota 1: "))
n2 =  float(input("Informe a nota 2: "))
n3 =  float(input("Informe a nota 3: "))
n4 =  float(input("Informe a nota 4: "))

media = (n1+n2+n3+n4)/4

if media < 5:
    print("Reprovado")
elif media >= 5 and media < 6.5:
    print("Recuperação")
elif media >= 6.5 and media < 9:
    print("Aprovado")
else:
    print("Aprovado com louvor.")
