# -*- coding: utf-8 -*-
cod1, num_peca1, valor_peca1 = map(float, input().split())
cod2, num_peca2, valor_peca2 = map(float, input().split())

total = (num_peca1 * valor_peca1) + (num_peca2 * valor_peca2)

print(f'VALOR A PAGAR: R$ {total:.2f}')