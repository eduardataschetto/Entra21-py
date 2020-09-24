x = False

while not(x):
    A, B, C = sorted(map(float, input().split()), reverse=True)
    if A > 0 and B > 0 and C > 0:
        x = True
    
if A >= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2 == B**2 + C**2:
        print('TRIANGULO RETANGULO')
    elif A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    elif A**2 < B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A == B and A == C:
        print('TRIANGULO EQUILATERO')
    elif A == B or A == C or B == C:
        print('TRIANGULO ISOSCELES')
