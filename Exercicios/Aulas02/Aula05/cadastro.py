from pessoas import Pessoa

def cadastrar_pessoa(cpf):
    nome = input("Nome: ")
    data_nasc = input("Data de Nascimento: ")
    telefone = input("Telefone: ")
    email = input("Email:")
    endereco = input("Endereço: ")
    pessoa = Pessoa(nome, cpf, email, endereco, data_nasc, telefone)
    salvar_arquivo(pessoa)
    return pessoa

def verifica_cpf (cpf):
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

def cadastrar_conta(pessoa):
    cpf = input("CPF: ")
    if verifica_cpf(cpf):
        pessoa = cadastrar_pessoa(cpf)
        
    else:
    print(f"O CPF {cpf} já consta no sistema.")


    pass

