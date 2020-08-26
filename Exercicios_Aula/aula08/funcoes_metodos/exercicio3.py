# 3) Estas 3 listas:
# 
# vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
# vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
# vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# 
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%
# 

vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo = [950.00, 89.90, 2500.00, 1750.00,500.00]

vendas = [vendas_armando, vendas_eduardo, vendas_paulo]
comissao_funcionarios = []
nome_vendedores = ['ARMANDO', 'EDUARDO','PAULO']

for i in vendas:
    if sum(i) <= 1000:
        comissao = 1
    elif sum(i) <= 2500:
        comissao = 1.5
    elif sum(i) <= 5000:
        comissao = 2
    else:
        comissao = 3
    comissao = sum(i) * (comissao / 100)
    comissao_funcionarios.append(comissao)

x = 0
for i in nome_vendedores:
    print(f'''
    {i}
    Média de vendas: R$ {sum(vendas[x]) / len(vendas[x])}
    Venda total: R$ {sum(vendas[x])}
    Quantidade de vendas: {len(vendas[x])}
    Comissão total: R$ {comissao_funcionarios[x]}
    ''')
    x += 1