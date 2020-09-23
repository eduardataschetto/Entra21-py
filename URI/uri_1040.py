w, x, y, z = map(float, input(). split())

media = (w*2 + x*3 + y*4 + z*1) / 10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n = float(input())
    print(f'Nota do exame: {n:.1f}')
    media = (media + n) / 2
    if media >= 5.00:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media:.1f}')