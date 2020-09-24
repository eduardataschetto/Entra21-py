def main():

    x = False
    while not(x):
        n = int(input())
        if n >= 1 and n <= 1 * 10**4:
            x = True

    for i in range(n):

        y = False
        while not(y):
            n1, op_um, d1, op, n2, op_dois, d2 = input().split()
            n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)
            
            if n1 >= 1 and n1 <= 1000 and d1 >= 1 and d1 <= 1000 and n2 >= 1 and n2 <= 1000 and d2 >= 1 and d2 <= 1000 and op_um == '/' and op_dois == '/' and (op ==  '+' or op == '-' or op == '*' or op == '/'):
                y = True

        if op == '+':
            numerador = (n1*d2 + n2*d1)
            denominador = (d1*d2)
        elif op == '-':
            numerador = (n1*d2 - n2*d1)
            denominador = (d1*d2)
        elif op == '*':
            numerador = (n1*n2) 
            denominador = (d1*d2) 
        else:
            numerador = (n1*d2)
            denominador = (n2*d1)
            
        num_simp = int(numerador / algoritmo_euclides(numerador, denominador))
        den_simp = int(denominador / algoritmo_euclides(numerador, denominador))


        print(f'{numerador}/{denominador} = {num_simp}/{den_simp}')

#Se n é múltiplo de m, então n é o MDC. Caso contrário, o MDC é o MDC de n e o resto da divisão de m por n
def algoritmo_euclides(numerador, denominador):
    if denominador == 0:
        return numerador
    else:
        return algoritmo_euclides(denominador, numerador%denominador)

if __name__=="__main__":
   main()