#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

funcionario = { 
                            'nome': 'Eduarda', 
                            'sobrenome': 'Taschetto', 
                            'cpf': '044.215.120-95', 
                            'rg': '4128245412', 
                            'salario': 5420.31
                        }

for chave, valor in funcionario.items():
    print(chave, ' - ', valor)


