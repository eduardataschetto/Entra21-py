def main():

    casos = int(input())
    for i in range(casos):
        
        num = input()
        qtd = 0
        for i in num:

            if i == '0': qtd += 6
            elif i == '1': qtd += 2
            elif i == '2': qtd += 5
            elif i == '3': qtd += 5
            elif i == '4': qtd += 4
            elif i == '5': qtd += 5
            elif i == '6': qtd += 6
            elif i == '7': qtd += 3
            elif i == '8': qtd += 7
            elif i == '9': qtd += 6
        print(f'{qtd} leds')

if __name__=='__main__':
   main()