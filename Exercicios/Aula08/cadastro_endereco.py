#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

def cadastrar_endereco(rua:str, numero:str, complemento:str, bairro:str, cidade:str, estado:str) -> str:

    if rua and numero and complemento and bairro and cidade and estado:
        
        arquivo = open('lista_dados.txt', 'a')
        arquivo.write(f",{rua},{numero},{complemento},{bairro},{cidade},{estado}\n")  
        arquivo.close()   

        return 'Endereço cadastrado com sucesso.'

    else:

        return 'Endereço inválido. Existem campos em branco. Tente novamente!'