# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)
from poo02 import Pessoa

class  Veiculo:

    passageiros = []

    def __init__(self, modelo, combustivel, marca, cor, placa):
        self.modelo = modelo
        self.combustivel = combustivel
        self.marca = marca
        self.cor = cor
        self.placa = placa

    def andar(self):
        return "Andando..."

    def acelerar(self, velocidade):
        return f'Acelerando a {velocidade}km/h.'

    def frear(self, velocidade):
        return f'Freando a {velocidade}km/h.'

    def som(self):
        return "Vrum"

    def adicionarPassageiro(self, person):
        self.passageiros.append(person)
        return self.passageiros

    def removerPassageiro(self, person):
        return self.passageiros


class Carro(Veiculo):

    def __init__(self,  modelo, combustivel, marca, cor, placa, cavalos):
        super().__init__(modelo, combustivel, marca, cor, placa)
        self.cavalos = cavalos


class Moto(Veiculo):

    def __init__(self,  modelo, combustivel, marca, cor, placa):
        super().__init__(modelo, combustivel, marca, cor, placa)

    def som(self):
        return "bizzzz"
        

class Caminhao(Veiculo):

    def __init__(self,  modelo, combustivel, marca, cor, placa, toneladas):
        super().__init__(modelo, combustivel, marca, cor, placa)
        self.toneladas = toneladas

    def som(self):
        return "vrummmmmmmmmm"


carro = Carro("Esportivo", "Gasolina", "Volkswagen", "Branco", "CARR-0101", "20")
print(carro.som())

caminhao = Caminhao("FH540", "Gasolina", "Volvo", "Branco", "FH540 -9999", "10")
print(caminhao.som())

moto = Moto("Biz", "Gasolina", "Honda", "Bege", "BIZZ-0101")
print(moto.som())

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

print(carro.adicionarPassageiro(p1))
print(carro.adicionarPassageiro(p2))
print(carro.adicionarPassageiro(p3))


print(carro.removerPassageiro(p1))



