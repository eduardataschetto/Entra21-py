from pessoas import Pessoa
from cadastro import cadastrar_conta, cadastrar_pessoa

class Banco():
    def __init__(self, nome):
        #lista bancos nome ai a pessoa só passa a opção
        self.nome = nome

class NuConta(Banco):
    def __init__(self, ):
        super().__init__()

class Viacredi(Banco):
    def __init__(self):
        super().__init__()

class Conta(Banco):
    def __init__(self, banco:Banco, pessoa:Pessoa, numero:str, agencia:str, tipo_conta:int, saldo:float, senha:str):
        super().__init__(banco)
        self.pessoa = pessoa
        self.numero = numero
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.senha = senha

    
if __name__ == "__main__":
    while True:
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Conta
            2 - Acessar Conta #senha, letra paara entra return numero, agencia                                                                                                                           
            # 2 - Visualizar Saldo
            # 3 - Fazer um depósito #Eduarda
            # 4 - Saque
            # 5 - Transferência
            3 - Sair\n"""))

        if valor == 1:
            cadastrar_conta()
        elif valor == 2:
            acessar_conta()
            
        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
