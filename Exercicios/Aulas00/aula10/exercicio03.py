"""Exercício 03

3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

3.2) Depois mostre os dados dos 5 clientes.

3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""

while True:
     nomes = []
     sexo = []
     idades = []
     id = []
#3.1
     for i in range(5):
        nomes.append(input('Informe o nome: '))
        sexo.append(input('Informe a sexo: '))
        idades.append(input('Informe a idade: '))
        id.append(i+1)

#3.2
     for i in range(5):
        print(f'''
        ID: {id[i]}
        Nome: {nomes[i]}
        Sexo: {sexo[i]}
        Idade: {idades[i]}
        ''')

#3.3
     x = int(input('Informe o ID do cliente a ser exibido: '))
     x = id.index(x)
     print(f'''
     ID: {id[x]}
     Nome: {nomes[x]}
     Sexo: {sexo[x]}
     Idade: {idades[x]}
     ''')
     
#3.4
     x =  int(input('Informe o ID do cliente para conferir as informações: '))
     x = id.index(x)
     if idades[x] < '17':
         print('Entrada proibida! ')
     else:
         print('Entrada liberada! ')
     if sexo[x] == 'Masculino' or  sexo[x] == 'masculino' or sexo[x] == 'm' or sexo[x] == 'M':
         print('5% de desconto. ')
     elif sexo[x] == 'Feminino' or  sexo[x] == 'feminino' or sexo[x] == 'f' or sexo[x] == 'F':
         print('50% de desconto. ')
     else:
         print('Opção não encontrada! ')
         y = input('Para continuar digite 1: ')
         if not(y == '1') or not(y):
            break