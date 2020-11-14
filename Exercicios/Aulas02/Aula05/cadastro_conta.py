from arquivo import limpa_tela, salvar_arquivo, filtrar_conta
from time import sleep
from random import randint
from pessoas import Pessoa


def cadastrar_pessoa():
    limpa_tela()
    print("########## CADASTRO DE PESSOA ##########\n")
    cpf = input("Informe seu CPF: ")
    if not dado_in_lista(1, cpf):
        nome = input("NOME: ")
        data_nasc = input("DATA DE NASCIMENTO: ")
        telefone = input("TELEFONE: ")
        email = input("E-MAIL:")
        endereco = input("ENDEREÇO: ")
        print('\n')
        pessoa = Pessoa(nome, cpf, email, endereco, data_nasc, telefone)
        salvar_arquivo(pessoa)
        return cpf
    return False


def cadastrar_conta():
    limpa_tela()
    print("########## CADASTRO DE CONTA ##########\n")
    cpf = cadastrar_pessoa()
    if cpf:
        banco = banco_select()
        print(f"Bem-vindo ao {banco}")
        print("Agora vamos gerenciar suas opções de segurança. ")
        sleep(1.5), limpa_tela()
        senha, pergunta_secreta, senha_pergunta, letras_secretas = cadastro_senhas()
        print(f"Obrigada pela preferência! Você ganhou um bônus no valor de R$ 20,00 por ter escolhido o {banco}!")
        
        while True:
            agencia = gera_dado_conta(1000)
            if not dado_in_lista(2, agencia):
                break

        while True:
            numero_conta = gera_dado_conta(100000)
            if not dado_in_lista(3, numero_conta):
                break
        with open("conta.txt", "a") as f:
            f.write(f"{banco};{cpf};{agencia};{numero_conta};{senha};20;{pergunta_secreta};{senha_pergunta};{letras_secretas}\n")
            f.close()
    else:
        print(f"O CPF já consta em nossos registros.")


def banco_select():
    bancos = ['NuBank', 'ViaCredi', 'Itaú', 'Santander', 'Bradesco']
    print("Para começar, informe o banco no qual você deseja abrir a conta:")
    while True:
        for i in range(len(bancos)):
            print(f"\t{i + 1} - {bancos[i]}")
        try:
            option = int(input("Informe a opção desejada: "))
            if option in [1, 2, 3, 4, 5]:
               return bancos[option - 1]
            limpa_tela()
        except ValueError as e:
            print("Ops! Algo deu errado. Tente novamente.")
            sleep(1.3), limpa_tela()


def cadastro_senhas():
    # cadastrando e validando senha
    while True:
        senha = input("Por favor, informe uma senha de 8 caracteres: ")
        if len(senha) == 8:
            break
    pergunta_secreta = input("Agora vamos definir uma pergunta secreta.\nInforme sua pergunta: ")
    senha_pergunta = input("Excelente pergunta. Informe a resposta: ")

    #cadastrando e valindo a letra secreta
    while True:
        letras_secretas = input("Informe as letras secretas: ")
        if not letras_secretas.isalpha():
            print("Ops! Aqui você só pode digitar letras.")
        else:
            break
    limpa_tela()

    #confirmando os dados
    while True:
        print(f"SENHA: {senha}\nPERGUNTA SECRETA: {pergunta_secreta.upper()}\nRESPOSTA DA PERGUNTA: {senha_pergunta}\nLETRAS SECRETAS: {letras_secretas.upper()}")
        valida_dados = int(input("Você confirma seus dados?\n 1 - SIM\t2 - EDITAR DADOS\n"))
        if valida_dados == 1:
            return senha, pergunta_secreta, senha_pergunta, letras_secretas
        elif valida_dados == 2:
            print('editar')
            #editar_dados(senha, pergunta_secreta, senha_pergunta, letras_secretas)
        else:
            print("Opção inválida! Tente novamente.")


def gera_dado_conta(max):
    dado = randint(0, max)
    return dado

#função que verifica se um determinado dado já foi cadastrado no arquivo
def dado_in_lista(index, dado):
    lista_dado = []
    with open("conta.txt", "r") as f:
        for linha in f:
            linha.strip()
            lista_dado.append(linha.split(";")[index])
        f.close()

        if dado in lista_dado:
            return True
        return False
