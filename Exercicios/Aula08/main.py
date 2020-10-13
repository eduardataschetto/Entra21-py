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

cadastrar_pessoa('eduarda', 'taschetto', 19, lista_pessoas)
cadastrar_endereco(3,'manoel', '242', 'casa', 'figueira', 'gaspar', 'sc', lista_pessoas)
pessoa_especifica(3, lista_pessoas)
lista_pessoas_cadastradas(lista_pessoas_cadastradas(lista_pessoas))
print(lista_pessoas)