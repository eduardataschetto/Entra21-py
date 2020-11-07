#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

def calcula_raiz(rad, indice):
     raiz = rad ** (1/indice)

     return raiz


def main():
    num = int(input('Informe um número: '))
    indice = int(input('Informe o indice: '))
    
    raiz = calcula_raiz(num, indice)
    print(f'A raiz de {num}, sob o indice {indice} é {raiz:.2f}.')


main()