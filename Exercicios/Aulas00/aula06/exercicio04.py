"""Execicios 04

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;

Triângulo Isósceles: quaisquer dois lados iguais;

Triângulo Escaleno: três lados diferentes;
"""

while True:
    try:
        a = float(input("Informe o lado A do triângulo: "))
        b = float(input("Informe o lado B do triângulo: "))
        c = float(input("Informe o lado C do triângulo: "))
        if ( a + b ) > c and ( a + c ) > b and ( b + c ) > a:
            if a == b and a == c:
                print ('Triângulo Equilatero')
            elif a == b or b == c or a == c:
                print ('Triângulo Isósceles')
            elif a !=b and c !=a and c!=b:
                print ('Triângulo Escaleno')
        else:
            print ('Os valores informados não formam um triângulo!')
    except ValueError:
        print('Oops! Valor inválido. Tente novamente. ')
    else:
        x = input('Digite 1 para continuar. ')
        if not(x == '1') or not(x):
            break