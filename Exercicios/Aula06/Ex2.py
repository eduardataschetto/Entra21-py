#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

print('SISTEMA DE CADASTRO DE FUNCIONARIOS DO ENTRA 21\n\n\n')

operacoes = {
        1: 'Cadastrar funcionário',
        2:  'Listar funcionários',
        3: 'Editar funcionário',
        4: 'Deletar funcionário',
        5: 'Sair'
}

while True:

    for chave, valor in operacoes.items():
        print('{}: {}'.format(chave, valor))
    op = int(input('\n\n\nInforme a operação desejada: '))
    print('\n\n')

    if op == 1:
        print('Você selecionou a opção cadastro de funcionário...')
    elif op == 2:
        print('Você selecionou a opção listar funcionário...')
    elif op == 3:
        print('Você selecionou a opção editar funcionário...')
    elif op == 4:
        print('Você selecionou a opção deletar funcionário...')
    elif op == 5:
        print('Você selecionou a opção sair...')
        break
    else:
        print('Opção inválida! Tente novamente.')
    print('\n\n\n')