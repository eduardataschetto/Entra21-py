from pessoas import Pessoa
from saque import saque
from deposito import fazer_deposito
from random import randint

def cadastrar_pessoa(cpf):
    nome = input("Nome: ")
    data_nasc = input("Data de Nascimento: ")
    telefone = input("Telefone: ")
    email = input("Email:")
    endereco = input("Endereço: ")
    pessoa = Pessoa(nome, cpf, email, endereco, data_nasc, telefone)
    salvar_arquivo(pessoa)
    return pessoa

def procurar_cpf (cpf):
    lista_cpfs = []
    #criando lista com os cpfs já cadastrados
    with open("pessoas.txt", "r") as file:
        for linha in file.readlines():
            lista_cpfs = linha.split(";")[0]

    #verificando se o cpf já costa nos registros
    if cpf in lista_cpfs:
        return False
    return True

def salvar_arquivo(pessoa):
    with open("pessoas.txt", "a") as file:
        file.write(f"{pessoa.cpf};{pessoa.nome};{pessoa.data_nasc};{pessoa.telefone};{pessoa.email};{pessoa.endereco}\n")
        file.close()

def cadastrar_conta():
    # Vai Começar a Criar as Senhas!
    pergunta_secreta = input('Qual Pergunta Secreta Deseja Ter?\nR: ').strip()
    resposta = input('\nE Qual Seria A Resposta?\nR: ').strip()
    senha = input('\nSua Senha de 7 Caractéres: ').strip()
    numconta = randint(1,9)
    numconta = str(numconta)
    
    quant = len(senha) # Vai Verificar A Quantidade de caracteres
    while quant != 7:
        print('\nERRO! Precisa Ser Exatamente 7 Caractéres!')
        senha = input('\nSua Senha de 7 Caractéres: ').strip() # Acabou A Verificação
        quant = len(senha)
    letras_secretas = input('\nQuais Seriam As Letras Secretas?\nR: ').strip().upper()
    print(f'Seu Número Da Conta é:{numconta}\nAnote Para Não Esquecer!!!')
    agencia = randint(1,9)
    
    agencia = str(agencia)
    # Vai Enviar Para o Arquivo txt
    p1 = Pessoa(nome, cpf, email, endereco, data_nasc, telefone, pergunta_secreta, resposta, senha, letras_secretas)

    file = open("pessoas.txt", "a")
    file.write(f"{p1.cpf};{p1.nome};{p1.data_nasc};{p1.telefone};{p1.email};{p1.endereco}\n")
    file.close()

    file = open('conta.txt', 'a')
    file.write(f'NuConta;{p1.cpf};{agencia};{numconta};{p1.senha};0;{p1.pergunta_secreta};{p1.resposta};{p1.letras_secretas}\n')
    file.close()


def acessar_conta():

    while True:
        numero_conta = input("Informe o número da conta: ")
        senha = input("Informe a senha: ")
        letra = input("Informe a senha de letra: ")

        option = int(input(f'''
        1 - Visualizar Saldo
        2 - Fazer um depósito #Eduarda
        3 - Saque
        4 - Transferência
        5 - Sair'''))

        if option == 1:
            visualizar_saldo(numero_conta)
        elif option == 2:
            fazer_deposito(numero_conta)
        elif option == 3:
            saque(numero_conta)
        elif option == 4:
            fazer_transferencia(numero_conta)
        else:
            break


def visualizar_saldo(numero_conta):
    file = open("conta.txt", "r")
    for procura in file: 
        linha = procura.strip()
        lista_conta = linha.split(";")
        if numero_conta == lista_conta[3]:
            print(f"Seu saldo é: {lista_conta[5]}")
    file.close()

