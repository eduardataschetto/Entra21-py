hora_inicio, hora_fim = map(int, input().split())

if hora_inicio == hora_fim:
    print('O JOGO DUROU 24 HORA(S)')
elif hora_inicio > hora_fim:
    print(f'O JOGO DUROU {24 - hora_inicio + hora_fim} HORA(S)')
else:
    print(f'O JOGO DUROU {hora_fim - hora_inicio } HORA(S)')