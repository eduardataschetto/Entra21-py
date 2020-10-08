#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

def calcula_raiz(x):

     raiz_quadrada = x ** (1/2)
     raiz_cubica = x ** (1/3)
     raiz_quarta = x ** (1/4)

     return raiz_quadrada, raiz_cubica, raiz_quarta


def main():
    x = int(input('Informe um número: '))

    raiz_quadrada, raiz_cubica, raiz_quarta = calcula_raiz(x)
    print(f'As raizes quadrada, cubica e quarta de {x} são, respectivamente, {raiz_quadrada}, {raiz_cubica} e {raiz_quarta} .')


main()