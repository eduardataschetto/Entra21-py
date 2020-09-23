cedula = [100, 50, 20, 10, 5, 2]
moeda = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
x = False

while not(x):
    valor = float(input())
    if 0 <= valor <= 1000000.00:
        valor += 0.001
        x = True

print('NOTAS:')
for i in cedula:
    qtdced = int(valor//i)
    print(f'{qtdced} nota(s) de R$ {i:.2f}')
    valor -= qtdced * i

print('MOEDAS:')
for j in moeda:
    qtdmod = int(valor// j)
    print(f'{qtdmod} moeda(s) de R$ { j:.2f}')
    valor -= qtdmod* j