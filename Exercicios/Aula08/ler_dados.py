
def ler_dados ():
    
    char = '*'
    print(f'{char*10} CADASTRO DE DADOS {char*10}')

    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    idade = int(input('Informe a idade: '))

    return nome, sobrenome, idade


def ler_endereco():

    char = '*'
    print(f'\n{char*10} ENDEREÇO {char*10}')

    rua = input('Rua: ')
    numero = input('Número: ')
    complemento = input('Complemento: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')

    return rua, numero, complemento, bairro, cidade, estado