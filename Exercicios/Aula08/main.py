#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#---       com seus respectivos endereços utilizando as funções do ex3 e ex4

from cadastro_pessoa import cadastrar_pessoa
from cadastro_endereco import cadastrar_endereco

from listar_pessoas import listar_pessoas, listar_pessoa_especifica
from listar_enderecos import listar_enderecos,  listar_endereco_epecifico

lista_pessoas = []

def ler_dados ():
    char = '*'
    print(f'{char*10} CADASTRO DE DADOS {char*10}')
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    idade = int(input('Informe a idade: '))

    return nome, sobrenome, idade


def ler_endereco():
    char = '*'
    print(f'\n{char*10} ENDEREÇO {char*10}')
    rua = input('Rua: ')
    numero = input('Número: ')
    complemento = input('Complemento: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')

    return rua, numero, complemento, bairro, cidade, estado


def main():

    while True:

        nome, sobrenome, idade = ler_dados()

        situacao_cadastro = cadastrar_pessoa(nome, sobrenome, idade, lista_pessoas)

        if type(situacao_cadastro)== int:
            rua, numero, complemento, bairro, cidade, estado = ler_endereco()
            cadastrar_endereco(situacao_cadastro, rua, numero, complemento, bairro, cidade, estado, lista_pessoas)
            
            x = input('\nPara continuar cadastrando digite Enter, para sair digite 0.\n')

            if x == '0':
                break
        else:
            print(situacao_cadastro + 'Tente novamente.')

    char = '*'
    print(f'{char*15} PESSOAS CADASTRADAS {char*15}')

    for pessoa in lista_pessoas:
        listar_pessoa_especifica(pessoa['id_usuario'], lista_pessoas)
        listar_endereco_epecifico( pessoa['id_usuario'], lista_pessoas)


main()