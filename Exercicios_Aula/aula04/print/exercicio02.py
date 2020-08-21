# Exercicio 2
# 
# Imprima o menu de uma aplicação de cadastro de pessoas
# 
# O menu deve conter as opções de Cadastrar, Alterar, listar pessoas, alem da opção sair
class Person:
    def __init__ (self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

def listar_pessoas():
    for i in pessoas:
            print(f'''    
            {str(pessoas.index(i))} - Nome = {i.name}
                Idade = {i.age}
                Telefone = {i.phone_number}''')

pessoas = [] 
while True:
    try:
        op = input('''
        1 - Cadastrar
        2 - Alterar cadastro
        3 - Listar pessoas
        DIGITE 0 PARA SAIR

        Informe a opção desejada:  ''')
        print('\n')
        if op == '1':
            name = str(input("Informe o nome da pessoa que você deseja cadastrar: "))
            age = int(input("Informe a idade: "))
            phone_number = int(input("Informe o número de telefone: "))
            pessoas.append(Person(name, age, phone_number))
        elif op == '2':
            if not(pessoas):
                print("Cadastre alguém primeiro!")
            else:
                print('ALTERAR CADASTRO')
                listar_pessoas()
                pessoa_alterar = int(input("Informe o número da pessoa que você deseja alterar: "))
                dado_alterar = input(f'''
                1 - Nome = {pessoas[pessoa_alterar].name}
                2 - Idade =  {pessoas[pessoa_alterar].age}
                3 - Telefone =  {pessoas[pessoa_alterar].phone_number}
                Informe o dado que você deseja alterar: ''')
                if dado_alterar == '1':
                    novo_dado = input("Qual será o novo nome? ")
                    pessoas[pessoa_alterar].name = novo_dado
                if dado_alterar == '2':
                    novo_dado = input("Qual será a nova idade? ")
                    pessoas[pessoa_alterar].age = novo_dado
                if dado_alterar == '3':
                    novo_dado = input("Qual será o novo número de telefone? ")
                    pessoas[pessoa_alterar].phone_number = novo_dado
        elif op == '3':
            listar_pessoas()
        else:
            break
    except ValueError:
        print('Opa! Parece que você digitou algo errado. Tente novamente.')