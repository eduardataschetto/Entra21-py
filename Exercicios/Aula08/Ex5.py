#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#---       com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1 import cadastrar_pessoa
from Ex2 import cadastrar_endereco
from Ex3 import lista_pessoas_cadastradas, pessoa_especifica
from Ex4 import listar_enderecos

lista_pessoas = []

cadastrar_pessoa('eduarda', 'taschetto', 19, lista_pessoas)
cadastrar_endereco(3,'manoel', '242', 'casa', 'figueira', 'gaspar', 'sc', lista_pessoas)
pessoa_especifica(3, lista_pessoas)
lista_pessoas_cadastradas(lista_pessoas_cadastradas(lista_pessoas))
print(lista_pessoas)