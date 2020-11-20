import sqlite3


class Pessoa():
    def __init__(self, nome: str, data_nascimento: str, cpf: str,
                 endereco: str, salario: float, profissao: str,
                 email: str, telefone: str, nome_de_responsavel: str,
                 sexo: str, naturalidade: str, nacionalidade: str):

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_de_responsavel = nome_de_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade

    def salvar_pessoa_na_tabela(self):

        conn = sqlite3.connect(
            'cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        tupla_dados_pessoa = (self.nome, self.data_nascimento,
                              self.cpf, self.endereco, self.salario,
                              self.profissao, self.email, self.telefone,
                              self.nome_de_responsavel, self.sexo,
                              self.naturalidade, self.nacionalidade)

        cursor.execute("""
                        INSERT INTO cadastro_de_pessoas (nome, data_nascimento, 
                                                        cpf, endereco, salario, profissao, email,
                                                        telefone, nome_de_responsavel, sexo, 
                                                        naturalidade, nacionalidade) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_pessoa)

        conn.commit()
        conn.close()


    def delete_pessoa(self):
        pass

    def update_pessoa(self):
        pass

    def exibir_pessoa(self):
        pass

    def insert_propriedade_pessoa(self):
        pass


class Carro():
    def __init__(self, nome_veiculo: str, marca: str, modelo_categoria: str,
                 cor: str, tipo_motor: str, combustivel: str, ano: int,
                 num_portas: int, qtd_passageiros: int, placa: str,
                 criado_em: str):

        self.nome_veiculo = nome_veiculo
        self.marca = marca
        self.modelo_categoria = modelo_categoria
        self.cor = cor
        self.tipo_motor = tipo_motor
        self.combustivel = combustivel
        self.ano = ano
        self.num_portas = num_portas
        self.qtd_passageiros = qtd_passageiros
        self.placa = placa
        self.criado_em = criado_em

    def salvar_veiculo_na_tabela(self):
        conn = sqlite3.connect(
            'cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        tupla_dados_veiculo = (self.nome_veiculo, self.marca, self.modelo_categoria,
                               self.cor, self.tipo_motor,
                               self.combustivel, self.ano, self.num_portas,
                               self.qtd_passageiros, self.placa,
                               self.criado_em)

        cursor.execute("""
                        INSERT INTO cadastro_de_veiculos (nome_veiculo, marca, 
                        modelo_categoria, cor, tipo_motor, combustivel, ano,
                        num_portas, qtd_passageiros, placa, criado_em)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_veiculo)

        conn.commit()
        conn.close()


# confirmação se a ação foi executada retornando mensagem
    def delete_veiculo(self):
        pass

  # confirmação se a ação foi executada retornando mensagem
    def update_veiculo(self):
        pass

    def exibir_veiculo(self):
        pass

  # confirmação se a ação foi executada retornando mensagem
    def insert_propriedade_veiculo(self):
        pass


# p = Pessoa('Raul', 12131993, 2222202002, 'lalala', 30.000, 'dev', 'arrarara@hha', 3232323, 'lsokaoska', 'm','cvel','br')
# p.salvar_pessoa_na_tabela()

# v = Carro('relampago mcqueen', 'm', 'mod', 'vermelho', '1.8', 'gasolina', 2020, 5, 3, '0444-555', '2020-07-11')
# v.salvar_veiculo_na_tabela()


option = input("")
conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT cadastro_de_pessoas.nome, cadastro_de_pessoas.cpf, cadastro_de_pessoas.telefone, cadastro_de_veiculos.placa, cadastro_de_veiculos.ano, cadastro_de_veiculos.modelo_categoria, cadastro_de_veiculos.id_veiculo FROM cadastro_de_pessoas
    INNER JOIN pessoa_veiculo ON pessoa_veiculo.id_proprietario = cadastro_de_pessoas.id_pessoa
    INNER JOIN cadastro_de_veiculos ON pessoa_veiculo.id_veiculo_prop = cadastro_de_veiculos.id_veiculo
    WHERE cadastro_de_pessoas.id_pessoa = ?
""", option)


for linha in cursor.fetchall():
    dados = list(linha)
    print(f"""
NOME: {dados[0]}
CPF: {dados[1]}
TELEFONE: {dados[2]}
PLACA: {dados[3]}
ANO: {dados[4]}
MODELO: {dados[5]}
""")
