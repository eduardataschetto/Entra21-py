import sqlite3

class Veiculo():

    def __init__(self, nome:str, marca:str, modelo:str, ano:str, placa:str, proprietario:str, num_portas:int, cor:str, km_rodado:str, qtd_passageiros:int, motor:str, combustivel:str, meio_locomocao:str, valor:str) -> None:
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.proprietario =  proprietario
        self.num_portas = num_portas
        self.cor = cor
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        self.valor = valor

        # def __str__(self) -> str:
        #     return f"{self.marca}_{self.modelo}_{self.placa}_{self.ano}_{self.motor}_{self.combustivel}_{self.proprietario}"

    def insert_veiculo(self) -> None:
        conn = sqlite3.connect('concessionaria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO veiculos (nome, marca, modelo, ano, placa, proprietario, num_portas, cor, km_rodado, qtd_passageiros, motor, combustivel, meio_locomocao, valor)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.marca, self.modelo, self.ano, self.placa, self.proprietario, self.num_portas, self.cor, self.km_rodado, self.qtd_passageiros, self.motor,  self.combustivel, self.meio_locomocao, self.valor))
        conn.commit()
        conn.close()


class Pessoa():

    def __init__(self, nome:str, data_nasc:str, cpf:str, endereco:str, salario:str, profissao:str, email:str, telefone:str, nome_resp:str, sexo:str, naturalidade:str, nacionalidade:str) -> None:
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_resp = nome_resp
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade


    def __str__(self) -> str:
        return f"{self.nome}_{self.data_nasc}_{self.cpf}_{self.endereco}_{self.salario}_{self.profissao}_{self.email}_{self.telefone}_{self.nome}_{self.sexo}_{self.naturalidade}_{self.nacionalidade}"

    def insert_pessoa(self) -> None:
        conn = sqlite3.connect('concessionaria.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pessoas (nome, data_nasc, cpf, endereco, salario, profissao, email, telefone, nome_resp, sexo, naturalidade, nacionalidade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", (self.nome, self.data_nasc, self.cpf, self.endereco, self.salario, self.profissao, self.email, self.telefone, self.nome_resp, self.sexo, self.naturalidade, self.nacionalidade))
        conn.commit()
        conn.close()