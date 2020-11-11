from veiculos import Carro, Moto, Caminhao
from pessoas import Pessoa

def cadastrarVeiculo():
    while True:
        option = int(input(f"1 - Carro\n2 - Moto\n3 - Caminhão\nInforme o veiculo que você deseja cadastrar: "))

        if option in [1, 2, 3]:
            modelo = input("Informe o modelo do veículo: ")
            comb = input("Informe o combustível: ")
            marca = input("Informe a marca: ")
            cor = input("Informe a cor: ")
            placa = input("Informe a placa: ")
            capacidade = int(input("Informe a capacidade de passageiros: "))

            if option == 1:
                cavalos = input("Informe quantos cavalos de potência o carro possui: ")
                carro = Carro(modelo, comb, marca, cor, placa, capacidade, cavalos)
                return carro
            elif option == 2:
                moto = Moto(modelo, comb, marca, cor, placa, capacidade)
                return moto
            else:
                toneladas = input("Informe quantas toneladas: ")
                caminhao = Caminhao(modelo, comb, marca, cor, placa, capacidade, toneladas)
                return caminhao
        else:
            print("Opção Inválida! Tente novamente.")


def cadastrarPassageiro(veiculo:Veiculo):

    if veiculo.capacidade >= len(veiculo.passageiros) + 1:
        nome = input("Informe o nome do passageiro: ")
        idade = input("Informe a idade: ")
        cpf = input("Informe o CPF: ")
        p = Pessoa(nome, idade, cpf)
        veiculo.adicionarPassageiro(p)
        imprimePassageiros(veiculo)
    else:
        print("Capacidade esgotada! Você deve remover algum passageiro para adionar um novo. ")


def imprimePassageiros(veiculo):
    print(f"PASSAGEIROS")
        for passageiro in veiculo.mostrarPassageiros():
            print(f'''Nome: {passageiro.nome} \nIdade: {passageiro.idade}\nCPF: {passageiro.cpf}\n''')


def main():
    while True:
        option = int(input("1- Cadastrar veículos\n1 - Adicionar passageiro\n2- Remover passageiro\nInforme a opção desejada: "))
        
        if option == 1:
            veiculo = cadastrarVeiculo()
            cadastrarPassageiro(veiculo)
        elif option == 2:
            cadastrarPassageiro(veiculo)
        elif option == 3:
            removerPassageiro()
        else:
            print("Opção inválida! Tente novamente: ")


# carro.adicionarPassageiro(p1)
# carro.adicionarPassageiro(p2)
# carro.adicionarPassageiro(p3)
# carro.adicionarPassageiro(p4)
# carro.adicionarPassageiro(p5)

# carro.removerPassageiro(p5)

# carro.mostrarPassageiros()


# carro = Carro("Esportivo", "Gasolina", "Volkswagen", "Branco", "CARR-0101", "20", 5)
# caminhao = Caminhao("FH540", "Gasolina", "Volvo", "Branco", "FH540 -9999", "10", 2)
# moto = Moto("Biz", "Gasolina", "Honda", "Bege", "BIZZ-0101", 2)


if __name__ == "__main__":
    main()
