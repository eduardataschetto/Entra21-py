# Exercicio 13
#
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
#
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
#
# Se o usuário selecionar 'Dados' deve aparecer o nome do cliente e a idade
#
# Se o usuário selecionar 'Endereço' deve aparecer o nome do cliente e o endereço
#
# Se o usuário selecionar 'Contato' deve aparecer o nome do cliente, email e o telefone
while True:
    try:
        nome_cliente = str(input('Informe seu nome: '))
        idade_cliente = int(input('Informe sua idade: '))
        endereco_cliente = input('Informe seu endereço: ')
        email_cliente = str(input('Informe seu email: '))
        tel_cliente = input('Informe seu telefone: ')
        op = int(input('''
            #################
            1 - Dados
            2 - Endereço
            3 - Contato
            #################
            Qual opção você deseja visualizar? '''))
        if op == 1:
            print(f'''
            Nome: {nome_cliente}
            Idade: {idade_cliente}
            ''')
        elif op == 2:
            print(f'''
            Nome: {nome_cliente}
            Endereço: {endereco_cliente}
            ''')
        elif op == 3:
            print(f'''
            Nome: {nome_cliente}
            Email: {email_cliente}
            Telefone: {tel_cliente}
            ''')
        break
    except ValueError:
        print('Oops! Valor inválido. Tente novamente: ')
    

