# -*- coding: utf-8 -*-
A, B, C = map(float, input().split(' '))

area_tri = (A * C) / 2
area_circ =  3.14159 * C ** 2
area_trap = ((A + B) * C) / 2
area_quad = B ** 2
area_ret = A * B

print(f'TRIANGULO: {area_tri:.3f}')
print(f'CIRCULO: {area_circ:.3f}')
print(f'TRAPEZIO: {area_trap:.3f}')
print(f'QUADRADO: {area_quad:.3f}')
print(f'RETANGULO: {area_ret:.3f}')