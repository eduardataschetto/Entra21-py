#Execicios 01
#Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições
#Venda Total
#de R$ 0.00 a R$ 30000.00 - 0%
#de R$ 30000.01 a R$ 50000.00 - 1.5%
#de R$ 50000.01 a R$ 100000.00 - 2.5%
#Acima de R$ 100000.00 - 3.5%

vendat = float(input("Informe a VEnda Total: "))

if vendat <= 30000.00:
    c =  0
elif vendat >=30000.01 and vendat <= 50000.00:
    c = 1.5
elif vendat >= 50000.01 and vendat <= 100000.00:
    c = 2.5
else:
    c = 3.5
 
comissao = c/100 * vendat
print("Sua comissão é de R$ "+str(comissao))


