A, B, C, D = map(int, input().split())

if B > C and D > A and C + D > B + A and C >= 0 and C >= 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")