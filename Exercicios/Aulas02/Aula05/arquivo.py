from os import system, name

__pessoas = open("pessoas.txt")

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
    f.close()


def update_contas(contas):
    with open("conta.txt", "w") as f:
        for conta in contas:
            f.write(f"{conta[0]};{conta[1]};{conta[2]};{conta[3]};{conta[4]};{conta[5]}\n")
    f.close()


def salvar_arquivo(pessoa):
    with open("pessoas.txt", "a") as file:
        file.write(f"{pessoa.cpf};{pessoa.nome};{pessoa.data_nasc};{pessoa.telefone};{pessoa.email};{pessoa.endereco}\n")
        file.close()


def valida_login(numero_conta, senha, letra):
    contas, index = filtrar_conta(numero_conta)
    if senha == contas[index][5] and letra == contas[index][5]:
        pass
    print(contas[index])


def limpa_tela() -> None:
    # for windows 
        if name == 'nt': 
            system('cls') 
    # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear')