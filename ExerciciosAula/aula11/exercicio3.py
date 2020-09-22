"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""
list = []

while True:
    nome = input('Informe seu nome: ')
    if not(nome):
        print('Oops! Nome em branco.')
        continue
    idade = input('Informe a idade: ')
    if not(idade):
        print('Obrigado pela preferência! ')
        break
    if int(idade) > 18:
        print('Entrada permitida! ')
        list.append(nome)
    else:
        print('Entrada proibida!')

print(list)
    