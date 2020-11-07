#--- Exercício 4  - Funções
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console

def imprime_cabecalho(char, nome_empresa):
    print(f'{char*10} {nome_empresa} {char*10}\n')

def imprime_rodape(char, nome_empresa):
    print(f'\n{char*10} A {nome_empresa} agradece sua preferência {char*10}')

def main():
    nome_empresa = input('Informe o nome da empresa: ')
    char = input('Informe um caractere: ')
    
    imprime_cabecalho(char, nome_empresa)
    imprime_rodape(char, nome_empresa)


main()