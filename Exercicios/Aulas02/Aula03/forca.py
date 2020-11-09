from os import system, name
from time import sleep
from random import randint

palavra = ""
dica = ""
chances = 0
no_repeat = []

def carregar_configuracoes() -> None:
    global palavra, chances, dica
    linhas_arquivo = []

    with open("./Exercicios/Aulas02/Aula03/forca.cfg", "r") as file:
        linhas_arquivo = file.readlines()
    linha = sort_linha(linhas_arquivo)
    palavra, chances, dica = str(linha[0]).upper(), int(linha[1]),  str(linha[2]).upper()
    file.close()


#e se não tiver mais palavras?
def sort_linha (linhas_arquivo:list) -> list:
   global no_repeat
   
   while True:
        index =  randint(0, len(linhas_arquivo) - 1)
        if not index in no_repeat:
            no_repeat.append(index)
            return linhas_arquivo[index].split(";")


def is_alphabet(palavra:str) -> bool:
    alfabeto = []
    for i in range(ord('a'), ord('z') + 1):
        alfabeto.append(chr(i).upper())

    for letra in palavra.split(" "):
        for char in letra:
            if not char.upper() in alfabeto:
                return False
    return True

    
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
    if  is_alphabet(chute) and not chute in letras_usadas and len(chute) == 1:
        return True

def tentar_novamente(letras_usadas:list) -> None:
    global chances, dica
    option = input("Deseja tentar novamente? Você terá 5 novas tentativas e uma dica.\n DIGITE 1 PARA CONTINUAR: ")

    if option == '1':
        chances = 5
        limpa_tela()
        print(f"DICA: {dica}")
        sleep(3)
        jogada(letras_usadas)


def jogar() -> None:
    global palavra, chances
    letras_usadas = []
    carregar_configuracoes()
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
            chute = input("Digite uma letra: ").upper()

            valid_chute = valida_chute(chute, letras_usadas)
            if valid_chute:
                letras_usadas.append(chute)
                if not chute in palavra:
                    chances -= 1
        else:
            break


def modificar_configuracoes(parametro:str) -> None:
    with open("./Exercicios/Aulas02/Aula03/forca.cfg", parametro) as file:
        while True:
            palavra = input("Informe a palavra: ")
            if is_alphabet(palavra):
                break
            print("Ops! Caractere inválido.Tente novamente.")

        dica = input("Que palavra difícil! Dê uma dica: ")

        while True:
            chances = input("Informe o número de chances: ")
            if chances.isdigit():
                break

    file.write(f'{palavra};{chances};{dica}\n')
    file.close()


def menu() -> str:
     while True:
        option = input(f'''
        1 - Jogar
        2 - Modificar configurações
        3 - Adicionar nova palavra
        4 - Sair
        ESCOLHA UMA OPÇÃO: ''')
        if option in ['1', '2', '3', '4']:
            return option
        else:
            print("Opção Inválida! Tente novamente. ")


def main() -> None:
    while True:
        option = menu()
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