#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def imprime_cabecalho(nome_empresa):
    char = '-'
    print(f'{char*10} Cadastro {nome_empresa} {char*10}')

def main ():
    nome_empresa = input('Informe o nome da empresa: ')
    imprime_cabecalho(nome_empresa)


main()