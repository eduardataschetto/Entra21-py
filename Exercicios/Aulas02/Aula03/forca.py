from os import system, name
from random import randint

palavra = ""
chances = 0

def carregar_configuracoes() -> None:
    global palavra, chances
    linhas_arquivo = []

    with open("./Exercicios/Aulas02/Aula03/forca.cfg", "r") as file:
        linhas_arquivo = file.readlines()
        linha = linhas_arquivo[randint(0, len(linhas_arquivo) - 1)].split(",")
        palavra = str(linha[0]).upper()
        chances = int(linha[1])


def limpa_tela() -> None:
    # for windows 
        if name == 'nt': 
            system('cls') 
    # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear')


def fim_jogo(tentativa_palavra:str, letras_usadas:list) -> bool:
    global palavra, chances

    if chances == 0:
        print("Você perdeu!")
        tentar_novamente(letras_usadas)
        return True
    elif tentativa_palavra == palavra:
        print("Você ganhou com apenas %d!" % chances)
        return True


def valida_chute(chute:str, letras_usadas:list) -> bool:
    if not(chute.isdigit() or chute in letras_usadas):
        return True

def tentar_novamente(letras_usadas:list) -> None:
    global palavra, chances
    option = input("Deseja tentar novamente? Você terá 5 novas tentativas.\n DIGITE 1 PARA CONTINUAR: ")

    if option == '1':
        chances = 5
        jogada(letras_usadas)

def jogar() -> None:
    global palavra, chances
    carregar_configuracoes()
    letras_usadas = []
    jogada(letras_usadas)


def jogada(letras_usadas:list) -> None:
    global palavra, chances

    while True:
        tentativa_palavra = ""
        limpa_tela()

        print("Número de chances: %d - tentativas:" % chances) # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")

        if not fim_jogo(tentativa_palavra, letras_usadas):
            chute = input("Digite uma letra:").upper()

            valid_chute = valida_chute(chute, letras_usadas)
            if valid_chute:
                letras_usadas.append(chute)
                if not chute in palavra:
                    chances -= 1
        else:
            break


def modificar_configuracoes(parametro:str) -> None:
    with open("./Exercicios/Aulas02/Aula03/forca.cfg", parametro) as file:
        palavra = input("Informe a palavra: ")
        chances = input("Informe o número de chances: ")
        file.write(f'{palavra},{chances}\n')
        file.close()


def imprime_menu() -> str:
     while True:
        option = input(f'''
        1 - Jogar
        2 - Resetar palavras
        3 - Adicionar nova palavra
        4 - Sair
        ESCOLHA UMA OPÇÃO: ''')
        if option in ['1', '2', '3', '4']:
            return option
        else:
            print("Opção Inválida! Tente novamente. ")

    
def main() -> None:
    while True:
        option = imprime_menu()
        if option == '1': 
            jogar()
        elif option == '2':
            modificar_configuracoes("w")
        elif option == '3':
            modificar_configuracoes("a")
        else:
            break


if __name__ == "__main__":
    main()