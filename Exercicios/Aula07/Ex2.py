#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

def divide(x, y):
    resultado = x/y
    print(f'{x}/{y} = {resultado}')

def main():

    while True:
        num1 = float(input('Informe um número: '))
        num2 = float(input('Informe outro número: '))

        if num1 != 0 and num2 != 0:
            break

    divide(num1, num2)


main()