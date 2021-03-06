#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#---       com seus respectivos endereços utilizando as funções do ex3 e ex4

from ler_dados import ler_dados, ler_endereco

from cadastro_pessoa import cadastrar_pessoa
from cadastro_endereco import cadastrar_endereco

from listar_pessoas import listar_pessoas, listar_pessoa_especifica
from listar_enderecos import listar_enderecos,  listar_endereco_epecifico


def main():

    while True:
        nome, sobrenome, idade = ler_dados()
        situacao_cadastro = cadastrar_pessoa(nome, sobrenome, idade)

        if situacao_cadastro != 'Ser humano menor de idade!':
            rua, numero, complemento, bairro, cidade, estado = ler_endereco()
            cadastrar_endereco(rua, numero, complemento, bairro, cidade, estado)
            
            x = input('\nPara continuar cadastrando digite Enter, para sair digite 0.\n')
            if x == '0':
                break
        else:
            print(situacao_cadastro + 'Tente novamente.')

    conteudo = 'PESSOAS CADASTRADAS'
    print(f'{conteudo:*^50}')

    listar_pessoas()

main()
