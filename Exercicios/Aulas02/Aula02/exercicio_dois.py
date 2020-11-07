# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 100, 2% de desconto
# se o valor for superior a 200, 5% de desconto
# se o valor for superior a 500, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética

dict = {
    'cadeira': 100,
    'arroz': 30.99,
    'aspirador': 350,
    'forno': 650,
    'chocolate': 150,
    'tapete': 550
}

#calculando valor total dos itens
total = sum(dict.values())

#aplicando o desconto
desconto = 0
if total > 100 and total < 200:
    desconto = 0.02
elif total < 500:
    desconto = 0.05
else:
    desconto = 0.10
total_final = total - (total * desconto)

#descobrindo o item mais caro
for key, value in dict.items():
    if dict[key] == max(dict.values()):
        item_mais_caro = key

#ordendando os itens da lista 
dict_ordenado = {}
for item in sorted(dict.keys()):
    dict_ordenado[item] = dict[item]

print(f'''Valor total da compra: R$ {total_final:.2f}
Item mais caro: {item_mais_caro} - R$ {dict.get(item_mais_caro)}
Itens: {dict_ordenado}''')

file = open('arquivo.txt', 'a')
for key, value in dict_ordenado.items():
    file.write(f'{key}:{value},')
file.close()
