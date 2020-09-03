'''
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:



***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
'''
nome = []
sexo = []
telefone = []

for i in range(5):
    nome.append(input('Informe o nome: '))
    sexo.append(input('Informe o sexo: '))
    telefone.append(input('Informe o número de telefone: '))

print('''
***********************************
Relatório de clientes cadastrados 
***********************************''')
for i in range(len(nome)):
    print(f'''Nome: {nome[i]}
Sexo: {sexo[i]}
Telefone: {telefone[i]}
***********************************''')