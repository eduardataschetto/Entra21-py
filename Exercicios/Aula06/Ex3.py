
#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

livro = {
    'titulo': 'A metamorfose',
    'edicao': '1°',
    'autor': 'Franz Kafka',
    'data_publicacao':  '01/11/2002',
    'p_um': '''Numa manhã, ao despertar de sonhos inquietantes, Gregor Samsa deu por si na
cama transformado num gigantesco inseto. Estava deitado sobre o dorso, tão
duro que parecia revestido de metal, e, ao levantar um pouco a cabeça, divisou
o arredondado ventre castanho dividido em duros segmentos arqueados, sobre
o qual a colcha dificilmente mantinha a posição e estava a ponto de escorregar
Comparadas com o resto do corpo, as inúmeras pernas, que eram miseravelmente
finas, agitavam-se desesperadamente diante de seus olhos.''',
    'p_dois': '''Que me aconteceu? - pensou. Não era um sonho. O quarto, um vulgar quarto hu-
mano, apenas bastante acanhado, ali estava, como de costume, entre as quatro pare-
des que lhe eram familiares. Por cima da mesa, onde estava deitado, desembrulhada
e em completa desordem, uma série de amostras de roupas: Samsa era caixeiro-
viajante, estava pendurada a fotografia que recentemente recortara de uma revista
ilustrada e colocara numa bonita moldura dourada.'''
    }

for chave, valor in livro.items():
    if chave == 'p_um' or chave == 'p_dois':
        print('\t', valor)
    else:
        print (chave, ':', valor)