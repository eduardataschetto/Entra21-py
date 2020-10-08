def main ():

    count_cidades = 0
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            count_cidades += 1

            qtd_moradores = []
            cons_total = []
            for i in range(0,n):
                qtd, consumo = map(int, input().split())
                qtd_moradores.append(qtd)
                cons_total.append(consumo)

            consumo_medio, total_moradores = 0.0, 0
            cons_pessoa = []
            for i in range(0, len(qtd_moradores)):
                cons_pessoa.append(cons_total[i]//qtd_moradores[i])
                consumo_medio += cons_total[i]
                total_moradores += qtd_moradores[i]

            consumo_medio /= total_moradores
            consumo_medio = consumo_medio - 0.005
            
            for i in range(len(cons_pessoa)):
                for j in range(i+1, len(cons_pessoa)-1):
                    if cons_pessoa[j] == cons_pessoa[i]:
                        qtd_moradores[i] += qtd_moradores[j]
                        cons_pessoa.pop(j)
                        qtd_moradores.pop(j)

            for i in range(len(cons_pessoa)):
                for j in range(i+1, len(cons_pessoa)):
                        if cons_pessoa[j] < cons_pessoa[i]:
                            aux = cons_pessoa[i]
                            cons_pessoa[i] = cons_pessoa[j]
                            cons_pessoa[j] = aux
                            aux = qtd_moradores[i]
                            qtd_moradores[i] = qtd_moradores[j]
                            qtd_moradores[j] = aux
            
            print(f'Cidade# {count_cidades}:')
            for i in range(len(cons_pessoa)):
                print(f'{qtd_moradores[i]}-{int(cons_pessoa[i])}', end=" ")
            print(f'\nConsumo medio: {consumo_medio:.2f} m3.')

if __name__ == "__main__":
    main()