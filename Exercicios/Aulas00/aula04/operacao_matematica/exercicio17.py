# Exercicio 17
# A formula de calculo de área de um circulo é:
# 
# area = pi*r²
# 
# Sabemos que:
# 
# pi = 3.14
# r = raio da circunferência em metros (float)
# 
# Crie um programa que peça ao usuário o raio e calcule a área da circunferência
# 
print('Esse é um programa que calcula o raio de uma circunferência.')
while True:
    try:
        raio = float(input("Informe o raio da circunferência: "))
        print(f'A área da circuferência é {3.14 * (raio ** 2)}m².')
        break
    except ValueError:
        print('Você informou um valor inválido. Tente novamente. ')