"""
2. for: soma de números
Peça 5 números ao usuário, um de cada vez, usando for. No final, mostre a soma e a média.
"""

soma=0
for iteracao in range(5):
    numero=int(input(f'Digite um número: '))
    soma+=numero
print(f'Total: {soma} ')
print(f'Média: {soma//5}')
