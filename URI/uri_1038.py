x, y = map(int, input().split())

valores = [4.00, 4.50, 5.00, 2.00, 1.50]

total = valores[x-1] * y

print(f'Total: R$ {total:.2f}')