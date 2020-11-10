class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome}-{self.idade}-{self.cpf}"

p1 = Pessoa("Eduarda", 18, 00)
p2 = Pessoa("Cleyton", 21, 155)
p3 = Pessoa("Felix", 25, 455)
