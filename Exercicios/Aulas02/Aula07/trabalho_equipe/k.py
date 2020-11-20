import sqlite3

conn = sqlite3.connect('veiculos.db')
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE veiculos (
#         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#         nome Varchar(50),
#         marca TEXT NOT NULL,
#         modelo TEXT NOT NULL,
#         cor TEXT,
#         placa VARCHAR(7),
#         proprietario VARCHAR(50),
#         num_portas INT,
#         km_rodado INT,
#         qtd_passageiros INT,
#         ano INTEGER,
#         valor INTEGER,
#         motor INT,
#         combustivel VARCHAR(20),
#         meio_locomocao VARCHAR(30)        
        
# );               
# """)

print('Tabela criada com sucesso.')
conn.close()

class Veiculo: 

    def __init__(self, nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor
        self.nome = nome
        self.placa = placa
        self.proprietario = proprietario
        self.num_portas = num_portas
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao
        
        self.lista = [(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao)]

    def salvar_veiculo(self):
        self.lista.append(veiculos)
    
        bd = sqlite3.connect('veiculos.db')
        sql = bd.cursor()
        
        sql.executemany('''
        INSERT INTO veiculos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''',lista)


#Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)
def cadastro_veiculos():
    print("\n\t_____CADASTRO DE VEÍCULOS___\n")
    nome = input('Nome do Carro: '),
    marca = input("Marca: "),
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    placa = input("Placa: ")
    proprietario = input("Nome do proprietário: ")
    num_portas = int(input("Número de portas: "))
    km_rodado = int(input("KM rodados: "))
    qtd_passageiros = int(input("Quantidade máxima de passageiros: "))
    ano = int(input("Ano: "))
    valor = int(input("Valor: R$ "))
    motor = float(input("Motor: "))
    combustivel = input("Tipo de combustível: ")
    meio_locomocao = input("Meio de locomoção: ")
    
    veiculos = Veiculo(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao)
    print(veiculos)
    return veiculos

cadastro_veiculos()