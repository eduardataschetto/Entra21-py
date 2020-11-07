#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

def calcula_media(x, y, z):
    media = (x + y + z) / 3
    print(f'A média aritmética entre {x}, {y} e {z} é {media}.')

def main():
    x = float(input('Informe um número: '))
    y = float(input('Informe outro número: '))
    z = float(input('Informe o último número: '))

    calcula_media(x, y, z)


main()