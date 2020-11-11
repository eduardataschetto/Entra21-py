from pessoas import Pessoa

def cadastrar_pessoa():
    nome = input("Nome: ")
    data_nasc = input("Data: ")
    cpf = input("Cpf")
    telefone = input("Tel")
    email = input("Email:")
    endereco = input("Endereco: ")
    p1 = Pessoa(id(nome), nome, cpf, email, endereco, data_nasc, telefone)
    salvar_arquivo(p1)
    return p1

def salvar_arquivo(pessoa):
    file = open("pessoas.txt", "a")
    file.write(f"{pessoa.id};{pessoa.nome};{pessoa.data_nasc};{pessoa.cpf};{pessoa.telefone};{pessoa.email};{pessoa.endereco}\n")
    file.close()

def cadastrar_conta(pessoa):
    pass

