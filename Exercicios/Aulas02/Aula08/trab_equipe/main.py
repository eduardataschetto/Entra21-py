from pessoa_veiculo import Pessoa, Carro
from os import system, name
import datetime
import sqlite3

def main () -> None:
    while True:
        op = int(input(f"""
        {'*'*10} CONCESSIONÁRIA DO VELHO HERROR {'*'*10}\n
        1 - Cadastrar pessoa
        2 - Cadastrar veículo
        3 - Deletar dados
        4 - Atualizar dados
        5 - Exibir dados
        6 - Sair

        Informe a opção desejada: """))

        if op == 1:
            limpa_tela()
            cadastrar_pessoa()
        elif op == 2:
            limpa_tela()
            cadastrar_veiculo()
        elif op == 3:
            limpa_tela()
            deletar_dados()
        elif op == 4:
            limpa_tela()
            atualizar_dados()
        elif op == 5:
            limpa_tela()
            exibir_dados()
        elif op == 6:
            break
        else:
            print("Opção inválida! Tente novamente.")


def cadastrar_pessoa() -> None:
    print(f"{'*'*10} CADASTRO DE PESSOA {'*'*10}")
    nome = input("NOME: ")
    data_nascimento = input("DATA DE NASCIMENTO: ")
    cpf = input("CPF: ")
    endereco = input("ENDEREÇO: ")
    salario = input("SALARIO: R$ ")
    profissao = input("PROFISSÃO: ")
    email = input("EMAIL: ")
    telefone = input("TELEFONE: ")
    nome_de_responsavel = input("NOME DO RESPONSÁVEL: ")
    sexo = input("SEXO: ")
    naturalidade = input("NATURALIDADE: ")
    nacionalidade = input("NACIONALIDADE: ")

    pessoa = Pessoa(nome, data_nascimento, cpf, endereco, salario, profissao, email, telefone, nome_de_responsavel,  sexo, naturalidade, nacionalidade)
    pessoa.salvar_pessoa_na_tabela()


def cadastrar_veiculo() -> None:
    print(f"{'*'*10} CADASTRO DE VEÍCULO {'*'*10}")
    nome_veiculo = input("NOME DO VEÍCULO: ")
    marca = input("MARCA: ")
    modelo_categoria = input("MODELO: ")
    cor = input("COR: ")
    tipo_motor = input("MOTOR: ")
    combustivel = input("COMBUSTÍVEL: ")
    ano = input("ANO: ")
    num_portas = input("NÚMERO DE PORTAS: ")
    qtd_passageiros = input("QUANTIDADE MÁXIMA DE PASSAGEIROS: ")
    placa = input("PLACA: ")

    now = datetime.datetime.now()
    criado_em = f"{now.year}-{now.month}-{now.day}"

    veiculo = Carro(nome_veiculo, marca, modelo_categoria, cor, tipo_motor, combustivel, ano, num_portas, qtd_passageiros, placa, criado_em)
    veiculo.salvar_veiculo_na_tabela()


def deletar_dados() -> None:
    try:
        op = int(input("""1 - Deletar proprietário\n2 - Deletar veículo\n\tInforme a opção desejada: """))
        if op == 1:
            delete_pessoa()
        elif op == 2:
            delete_veiculo()
        else:
            print("Opção inválida.")
    except ValueError as e:
        print(e)


def atualizar_dados() -> None:
    try:
        op = int(input("""1 - Atualizar proprietário\n2 - Atualizar veículo\n\tInforme a opção desejada: """))
        if op == 1:
            update_pessoa()
        elif op == 2:
            update_veiculo()
        else:
            print("Opção inválida.")
    except ValueError as e:
        print(e)


def exibir_dados() -> None:
    try:
        op = int(input("""1 - Exibir proprietário\n2 - Exibir veículo\n\tInforme a opção desejada: """))
        if op == 1:
            exibir_pessoa()
        elif op == 2:
            exibir_veiculo()
        else:
            print("Opção inválida.")
    except ValueError as e:
        print(e)


def limpa_tela() -> None:
        if name == 'nt': 
            system('cls') 
        else: 
            system('clear')


if __name__ == "__main__":
        conn = sqlite3.connect(
        'cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM cadastro_de_veiculos
        """)
        print(cursor.fetchall())
        conn.close()