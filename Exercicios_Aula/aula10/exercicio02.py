"""Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

id: 3
Nome: Pedro


ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""
while True:
    try:
        nomes = []
        idades = []
        id = []
        x = int(input('Informe o número de clientes que você deseja cadastrar: '))
        for i in range(x):
            nomes.append(input('Informe o nome: '))
            idades.append(input('Informe a idade: '))
            id.append(i+1)
        for i in range(len(nomes)):
            print(f'''
            ID: {id[1]}
            Nome: {nomes[i]}
            Idade: {idades[i]}
            ''')
        
    except ValueError:
        print('Oops! Valor inválido. Por favor, informe apenas números inteiros. ')
    else:
        y = input('Para continuar digite 1: ')
        if not(y == '1') or not(y):
            break

    
    