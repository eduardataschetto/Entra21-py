class Carro:

    def __init__ (self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def acelerando(self, velocidade):
        print(f'Acelerando a {velocidade}km\h...')

    def freando(self, velocidade):
        print(f'Freando a {velocidade}km\h...')

if __name__ == "__main__":
    c = Carro('Ford', 'Mustang', 2020, 'Laranja')
    c.acelerando(20)
    c.freando(40)


class Gato:

    def __init__ (self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def miando(self):
        print('Minhau minhau')

if __name__ == "__main__":
    gato = Gato('Pandora', '2', 'Siamês')
    gato.miando()


class Celular:

    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligando(self):
        print('Ligando...')
    
if __name__ == "__main__":
    celular = Celular('Motorola', 'Moto G', 2020)
    celular.ligando()


class Quadrado:

    num_lados = 4

    def __init__ (self, cor, tam_lado, diagonal):
        self.cor = cor
        self.tam_lado = tam_lado
        self.diagonal = diagonal

    def calculaArea(self):
        print(f'Area = {self.tam_lado ** 2}')

    def calculaPerimetro(self):
        print(f'Perimetro = {self.tam_lado * num_lados}')

if __name__ == "__main__":
    quadrado = Quadrado('Amarelo', 4, 2)
    quadrado.calculaArea()
    quadrado.calculaPerimetro()


class Monitor:

    def __init__ (self, largura, altura, marca):
        self.largura = largura
        self.altura = altura
        self.marca = marca

    def ligar(self):
        print("Ligando...")

if __name__ == "__main__":
    monitor = Monitor(1080, 920, 'Dell')
    monitor.ligar()