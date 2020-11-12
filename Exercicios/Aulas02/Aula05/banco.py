from pessoas import Pessoa
from cadastro import cadastrar_conta, cadastrar_pessoa

class Banco():
    def __init__(self, nome):
        #lista bancos nome ai a pessoa só passa a opção
        self.nome = nome

# class NuConta(Banco):
#     def __init__(self, ):
#         super().__init__()

# class Viacredi(Banco):
#     def __init__(self):
#         super().__init__()

class Conta(Banco):
    def __init__(self, banco:Banco, pessoa:Pessoa, numero:str, agencia:str, tipo_conta:int):
        super().__init__(banco)
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
            #retirar, transferencia
            3 - Fazer um depósito
            4 - Sair\n"""))

        if valor == 1:
            pessoa = cadastrar_pessoa()
            cadastrar_conta(pessoa)
            
        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
