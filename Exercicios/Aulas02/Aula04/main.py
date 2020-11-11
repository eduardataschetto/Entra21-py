from veiculos import Carro, Moto, Caminhao
from pessoas import Pessoa

carro = Carro("Esportivo", "Gasolina", "Volkswagen", "Branco", "CARR-0101", "20", 5)
print(carro.som())

caminhao = Caminhao("FH540", "Gasolina", "Volvo", "Branco", "FH540 -9999", "10", 2)
print(caminhao.som())

moto = Moto("Biz", "Gasolina", "Honda", "Bege", "BIZZ-0101", 2)
print(moto.som())

p1 = Pessoa("Eduarda", 18, "044.215.130-96")
p2 = Pessoa("Maria Julia", 18, "044.215.130-96")
p3 = Pessoa("Pamela", 18, "044.215.130-96")
p4 = Pessoa("João", 21, "044.215.130-96")
p5 = Pessoa("Emily", 25, "044.215.130-96")
p6 = Pessoa("Cleiton", 15, "044.215.130-96")

carro.adicionarPassageiro(p1)
carro.adicionarPassageiro(p2)
carro.adicionarPassageiro(p3)
carro.adicionarPassageiro(p4)
carro.adicionarPassageiro(p5)

carro.removerPassageiro(p5)

carro.mostrarPassageiros()
