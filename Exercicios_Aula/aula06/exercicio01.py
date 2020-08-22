# Execicios 01
# Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições
# Venda Total
# de R$ 0.00 a R$ 30000.00 - 0%
# de R$ 30000.01 a R$ 50000.00 - 1.5%
# de R$ 50000.01 a R$ 100000.00 - 2.5%
# Acima de R$ 100000.00 - 3.5%

class Vendedor:
    def __init__(self, id, nome, vendatotal, comissao):
        self.id = id
        self.nome = nome
        self.vendatotal = vendatotal
        self.comissao = comissao

def cadastrar_vendedor(lista_vendedores):
    id_vendedor = int(input('Informe o ID do vendedor: '))
    nome_vendedor = str(input('Informe o nome do vendedor: '))
    venda_total = float(input("Informe o valor da venda total do vendedor: "))
    comissao = calcula_comissao(venda_total)
    lista_vendedores.append(Vendedor(id_vendedor, nome_vendedor, venda_total, comissao))

def calcula_comissao(venda_total):
    if venda_total <= 30000.00:
        porc_comissao = 0
    elif venda_total >= 30000.01 and venda_total <= 50000.00:
        porc_comissao = 1.5
    elif venda_total >= 50000.01 and venda_total <= 100000.00:
        porc_comissao = 2.5
    else:
        porc_comissao = 3.5
    comissao = venda_total * (porc_comissao/100)
    return comissao

def exibir_lista(lista_vendedores):
     if not(lista_vendedores):
        print('É necessário ter pelo menos um vendedor cadastrado para exibir a lista. Faça o cadastro.')
     else:
        for i in lista_vendedores:
            print(f'''    
            {str(lista_vendedores.index(i))} - Nome = {i.nome}
            ID = {i.id}
            Venda Total = R$ {i.vendatotal}
            Comissão = R$ {i.comissao}''')

def exibir_dados(lista_vendedores, vendedor):
    print(f'''
    1 - Nome = {lista_vendedores[int(vendedor)].nome}
    2 - ID = {lista_vendedores[int(vendedor)].id}
    3 - Venda Total = R$ {lista_vendedores[int(vendedor)].vendatotal}
    4 - Comissão = R$ {lista_vendedores[int(vendedor)].comissao}
    ''')

def alterar_cad(lista_vendedores):
    exibir_lista(lista_vendedores)
    vendedor = int(input('Informe o número do cadastro a ser alterado: '))
    exibir_dados(lista_vendedores, vendedor)
    alterar_dado = int(input('Informe o númerodo dado que você deseja alterar: '))
    if alterar_dado == 1:
        lista_vendedores[int(vendedor)].nome = str(input('Qual será o novo nome?'))
    if alterar_dado == 2:
       lista_vendedores[int(vendedor)].id = int(input('Qual será o novo ID? '))
    if alterar_dado == 3:
        lista_vendedores[int(vendedor)].vendatotal = float(input('Qual será o novo valor da venda total?'))
    if alterar_dado == 4:
        lista_vendedores[int(vendedor)].comissao = float(input('Qual será o novo valor da comissão? '))
    exibir_dados(lista_vendedores, vendedor)

def main():
    print('PROGRAMA PARA CALCULAR A COMISSÃO DE VENDEDORES')
    lista_vendedores = []
    while True:
        try:
            op = int(input('''
            1 - Cadastrar vendedor
            2 - Exibir lista
            3 - Alterar cadastro
            DIGITE 0 PARA SAIR

            Informe a operação desejada: 
            '''))
            if op == 1:
                cadastrar_vendedor(lista_vendedores)
            elif op == 2: 
                exibir_lista(lista_vendedores)
            elif op == 3:
                alterar_cad(lista_vendedores)
            elif op == 0:
                break
        except ValueError:
            print('Valor inválido. Tente novamente.')

main()