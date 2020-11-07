# Crie uma lista com todas as letras do alfabeto

# Remova as vogais dessa lista e crie uma tupla com elas

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito

alfabeto = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vogais = []

for letra in alfabeto:
    if letra == 'a' or letra == 'e' or letra == 'i'  or letra == 'o'  or letra == 'u':
        vogais.append(alfabeto.pop(alfabeto.index(letra)))

vogais = tuple(vogais)

print(alfabeto)
print(vogais)

eu = []
letras = [alfabeto, vogais]
for l in letras:
    for letra in l:
        if letra == 'e' or letra == 'd' or letra == 'u'  or letra == 'a'  or letra == 'r':
            eu.append(letra)

eu.append(18)
eu.append('livro')
eu = set(eu)

print(eu)
