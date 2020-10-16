#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve exibir todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#    a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id

dados = ['ID','NOME','SOBRENOME','IDADE','RUA','Nº','COMPLEMENTO','BAIRRO','CIDADE','ESTADO']

def listar_pessoas() -> None:

    arquivo = open('lista_dados.txt','r')

    for linha in arquivo:
        elemento = linha.split(',')
        for i in range(len(elemento)):
            print(f'{dados[i]}: {elemento[i]}')

    arquivo.close()


def listar_pessoa_especifica(id_usuario:str) -> None:

    arquivo = open('lista_dados.txt', 'r')

    for linha in arquivo:
        elemento = linha.split(',')
        if id_usuario in elemento:
            for i in range(len(elemento)):
                print(f'{dados[i]}: {elemento[i]}')

    arquivo.close()