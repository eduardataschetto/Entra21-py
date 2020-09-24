valido = False

while True:

    while not(valido):
        n = map(int, input().split())
        if n >= 1 and n <= 1 * 10**6:
            valido = True
        elif n == 0:
            break

    for i in range(n):
        valido = False
        while not(y):
            x, y = map(int, input().split())
            if x >= 1 and x <= 10 and y >= 1 and y <= 200:
                valido = True

            