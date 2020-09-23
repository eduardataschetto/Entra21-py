segundos = int(input())

horas = segundos // 3600
segundos = segundos - (horas * 3600)
minutos = segundos // 60
segundos = segundos - (minutos * 60)

print(f'{horas}:{minutos}:{segundos}')