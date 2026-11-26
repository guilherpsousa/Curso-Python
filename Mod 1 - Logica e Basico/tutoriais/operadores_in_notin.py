""" 
OPERADORES in e not in 
in = está entre
not in = não está entre
Strings são iteráveis, é como um vetor do portugol, consigo percorrer letra por letra
  0 1 2 3 4 5 6 7 8
  G u i l he r m e
 -9-8-7-6-5-4-3-2-1
"""

nome='Guilherme'
print(nome[0])
print(nome[-8])
print(nome[2])
print('G' in nome) # (A letra 'G' está no nome?) = True
print('G' not in nome) # (A letra 'G' não está no nome?) = False pois ela está no nome
print(15*'-') # só pra fazer uma divisória

nome2=input('Digite seu nome: ')
encontrar=input('Digite oque seja encontrar: ')


if encontrar in nome2:
    print(f'{encontrar} esta no {nome2}')
elif encontrar not in nome2: # só pra demonstrar o not in (mais fácil seria usar else no lugar de elif)
    print(f'{encontrar} não esta em {nome2}')
