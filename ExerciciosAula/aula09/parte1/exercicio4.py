"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""
while True:
    cadastro_pessoas = []
    for i in range (3):
        nome = input('Informe o nome: ')
        idade = input('Informe a idade: ')
        email = input('Informe o e-mail: ')
        lista = [nome, idade, email]
        cadastro_pessoas.append(lista)
    for i in cadastro_pessoas:
        print(i)
    x = input('Informe 1 para continuar: ')
    if not(x == '1') or not(x):
        break