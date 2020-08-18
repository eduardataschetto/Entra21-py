# Exercicio 13
#
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
#
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
#
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
#
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
#
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
endereco = input("Informe seu endereço: ")
email = input("Informe seu email: ")
tel = input("Informe seu telefone: ")


def dados():
    op = input("""
    #################
    Dados
    Endereço
    Contato
    #################
    Qual opção você deseja visualizar? 
    """)
    return op

def conf():
    op = dados()
    if op == 'Dados':
        print("Nome: "+nome+"\n Idade: "+idade)
    elif op == 'Endereço':
        print("Nome: "+nome+ "\n Endereço: "+endereco)
    elif op == 'Contato':
        print("Nome: "+nome+ "\n Email: "+email+ "\n Telefone: "+tel)
    else:
        print("Opção Inválida! Tente novamente:")
        conf()

conf()

