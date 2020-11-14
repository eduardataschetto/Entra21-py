from cadastro_conta import cadastrar_conta
from acessar_conta import acessar_conta
from pessoas import Pessoa
from arquivo import limpa_tela

class Conta():
    def __init__(self, banco, pessoa:Pessoa, numero:str, agencia:str, tipo_conta:int, saldo:float, senha:str):
        self.banco = banco
        self.pessoa = pessoa
        self.numero = numero
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.senha = senha

    
if __name__ == "__main__":
    while True:
        limpa_tela()
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Conta
            2 - Acessar Conta
            3 - Sair\n"""))

        if valor == 1:
            limpa_tela()
            cadastrar_conta()
        elif valor == 2:
            limpa_tela()
            acessar_conta()
        elif valor == 3:
            limpa_tela()
            print("Agradecemos a sua visita!")
            break
        else:
            print("Opção inválida!\n Tente novamente!")
