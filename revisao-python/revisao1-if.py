"""
1. if: par ou ímpar
Peça um número ao usuário e mostre se ele é par ou ímpar. 
Se for par e maior que 100, mostre também “Número grande”.
"""

numero=int(input('Digite um número: '))
if numero %2==0 and numero < 100:
    print('Seu número é par.')
elif (numero %2==0) and numero >= 100:
    print('Seu número é par, e também grande.')