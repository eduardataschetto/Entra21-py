class Pessoa:

    def __init__(self, nome, cpf, email, endereco, data_nasc, telefone):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco


    def __str__(self):
        return f"{self.id}_{self.nome}_{self.data_nasc}_{self.cpf}_{self.email}_{self.telefone}_{self.endereco}"