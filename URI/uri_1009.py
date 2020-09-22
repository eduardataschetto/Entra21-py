# -*- coding: utf-8 -*-
nome = input()
sal_fixo = float(input())
total_vendas = float(input())

sal_final = sal_fixo + (total_vendas * 0.15)

print(f'TOTAL = R$ {sal_final:.2f}')