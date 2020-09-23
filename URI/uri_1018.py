valor = int(input())

aux = valor
cedulas = [100, 50, 20, 10, 5, 2, 1]
qtdenotas = []

for i in cedulas:
    nota = aux // i
    aux = aux - (nota * i)
    qtdenotas.append(nota)

print(f'{valor}')
print(f'{qtdenotas[0]} nota(s) de R$ 100,00')
print(f'{qtdenotas[1]} nota(s) de R$ 50,00')
print(f'{qtdenotas[2]} nota(s) de R$ 20,00')
print(f'{qtdenotas[3]} nota(s) de R$ 10,00')
print(f'{qtdenotas[4]} nota(s) de R$ 5,00')
print(f'{qtdenotas[5]} nota(s) de R$ 2,00')
print(f'{qtdenotas[6]} nota(s) de R$ 1,00')