# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)

class  Veiculo:

    def __init__(self, modelo, combustivel, marca, cor, placa, capacidade):
        self.modelo = modelo
        self.combustivel = combustivel
        self.marca = marca
        self.cor = cor
        self.placa = placa
        self.capacidade = capacidade
        self.passageiros = []

    def __str__(self) -> None:
        return f"{self.modelo}_{self.combustivel}_{self.marca}_{self.cor}_{self.placa}_{self.capacidade}"

    def andar(self) -> None:
        return "Andando..."

    def acelerar(self, velocidade:float) -> None:
        return f'Acelerando a {velocidade}km/h.'

    def frear(self, velocidade:float) -> None:
        return f'Freando a {velocidade}km/h.'

    def som(self):
        return "vrumm"

    def adicionarPassageiro(self, pessoa:Pessoa) -> None:
        self.passageiros.append(pessoa)


    def removerPassageiro(self, pessoa:Pessoa) -> None:
        self.passageiros.remove(pessoa)

    def mostrarPassageiros(self) -> list:
        return self.passageiros

class Carro(Veiculo):

    def __init__(self,  modelo, combustivel, marca, cor, placa, cavalos, capacidade):
        super().__init__(modelo, combustivel, marca, cor, placa, capacidade)
        self.cavalos = cavalos


class Moto(Veiculo):

    def __init__(self,  modelo, combustivel, marca, cor, placa, capacidade):
        super().__init__(modelo, combustivel, marca, cor, placa, capacidade)
        

class Caminhao(Veiculo):

    def __init__(self,  modelo, combustivel, marca, cor, placa, toneladas, capacidade):
        super().__init__(modelo, combustivel, marca, cor, placa, capacidade)
        self.toneladas = toneladas
