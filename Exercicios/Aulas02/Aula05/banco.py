from pessoas import Pessoa
from cadastro import cadastrar_conta, cadastrar_pessoa

class Banco():
    def __init__(self, nome, cnpj):
        pass

    def cadastrar_conta():
        pass

class NuConta(Banco):
    def __init__(self, ):
        super().__init__()

class Viacredi(Banco):
    def __init__(self):
        super().__init__()

class Conta():
    def __init__(self, banco:Banco, pessoa:Pessoa, numero:str, agencia:str, tipo_conta:int):
        self.banco = banco
        self.pessoa = pessoa
        self.numero = numero
        self.agencia = agencia
        self.tipo_conta = tipo_conta
    


if __name__ == "__main__":
    while True:
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Conta
            2 - Visualizar Saldo
            3 - Fazer um depósito
            4 - Sair\n"""))

        if valor == 1:
            person = cadastrar_pessoa()
            cadastrar_conta(person)
            
        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
