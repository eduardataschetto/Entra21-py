from classes import Veiculo, Pessoa


carro = Veiculo('relampago mcqueen', 'carros', 'MOD', '2020', 'PLAC-0000', 'EDU', 4, 'VERMELHO', '20000', 5, 'COMBUSTAO', 'GASOSA', 'TERRESTRE', 200)
carro.insert_veiculo()

pessoa = Pessoa('Eduardaa', '2002-11-01', '044', 'Gaspar', 5000, 'dev', 'eduarda@gmail.com', '47991524115', 'no', 'F', 'são gabriel', ' br')
pessoa.insert_pessoa()

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
    
    veiculo = Veiculo(nome, marca, modelo, cor, placa, proprietario, num_portas, km_rodado, qtd_passageiros, ano, valor, motor, combustivel, meio_locomocao)
    