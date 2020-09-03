"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----



Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""

nome = []
idade = []
sexo = []
telefone = []

while True:
    op = input('''
-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----
Digite a opção desejada: ''')

    if op == 'A':
        nome.append(input('Infome o nome: '))
        idade.append(input('Infome a idade: '))
        sexo.append(input('Informe o sexo: '))
        telefone.append(input('Informe o telefone: '))
    elif op == 'B':
        print(nome)
    elif op == 'C':
        nome_cliente = input('Informe o nome do cliente: ')
        x = nome.index(nome_cliente)
        print(f' Nome: {nome[x]} \n Idade: {idade[x]} \n Sexo: {sexo[x]} \n Telefone: {telefone[x]}')
    elif op == 'D':
        nome_cliente = input('Informe o nome do cliente cujo cadastro você deseja deletar: ')
        if nome_cliente in nome:
            x = nome.index(nome_cliente)
            telefone.remove(telefone[x])
            sexo.remove(sexo[x])
            idade.remove(idade[x])
            nome.remove(nome[x])
        else:
            print('Nome não encontrado! ')
    elif op == 'S':
        break
    else:
        print('Oops! Opção inválida!')