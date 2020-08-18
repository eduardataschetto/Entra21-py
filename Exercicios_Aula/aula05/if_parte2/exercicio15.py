# Exercicio 15
# Crie um programa que peça ao usuário que digite um número de 1 a 12 e mostre o mês correspondente ao número.
# 
def selec ():
    dia = input("Informe um número de 1 a 12: ")
    return dia

def con ():
    dia = selec()
    if dia == '1':
        print("Janeiro")
    elif dia == '2':
        print("Fevereiro")
    elif dia == '3':
        print("Março")
    elif dia == '4':
        print("Abril")
    elif dia == '5':
        print("Maio")
    elif dia == '6':
        print("Junho")
    elif dia == '7':
        print("Julho")
    elif dia == '8':
        print("Agosto")
    elif dia == '9':
        print("Setembro")
    elif dia == '10':
        print("Outubro")
    elif dia == '11':
        print("Novembro")
    elif dia == '12':
        print("ENTÃO É NATAAAAAAAAAAAL")
        print("É TEMPO DE LUZ")
        print("brincadeira é só dezembro mesmo")
    else:
        print("Opção Inválida meu caro amigo.")
        print("Mas não fique triste e tente novamente: ")
        con()

con()