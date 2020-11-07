import datetime 

def calculaIdade(dia, mes, ano):
    now = datetime.datetime.now()
    idade = now.year - ano

    if now.month <= mes:
        if now.day <= dia:
            idade -= 1

    return idade

print(calculaIdade(1, 11, 2002))