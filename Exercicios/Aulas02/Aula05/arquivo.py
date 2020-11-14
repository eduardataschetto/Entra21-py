from os import system, name

def filtrar_conta(numero_conta:str) -> list:
    contas = []

    with open("conta.txt", "r") as f:
        for linha in f:
            linha = linha.strip()
            conta = linha.split(";")
            contas.append(conta)

        for conta in contas:
            if conta[3] == numero_conta:
                return contas, contas.index(conta)
    return False, False


def update_contas(contas):
    with open("conta.txt", "w") as f:
        for conta in contas:
            f.write(f"{conta[0]};{conta[1]};{conta[2]};{conta[3]};{conta[4]};{conta[5]};{conta[6]};{conta[7]};{conta[8]}\n")
    f.close()


def salvar_arquivo(pessoa):
    with open("pessoas.txt", "a") as file:
        file.write(f"{pessoa.cpf};{pessoa.nome};{pessoa.data_nasc};{pessoa.telefone};{pessoa.email};{pessoa.endereco}\n")
        file.close()


def limpa_tela() -> None:
    # for windows 
        if name == 'nt': 
            system('cls') 
    # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear')


def filtrar_pessoa(cpf):
    with open("pessoas.txt", "r") as f:
        for linha in f:
            linha = linha.strip().split(";")
            if linha[0] == cpf:
                pessoa = linha
                return pessoa
