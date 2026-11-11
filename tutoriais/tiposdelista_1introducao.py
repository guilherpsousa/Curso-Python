""" Listas em Python (fatiamento, redefinindo)
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Útil para índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#        0    1       2            3    4
#       -5   -4      -3           -2   -1
lista = [123, True, 'Guilherme',  1.2, []]

print('Lista inteira:', lista) #print na lista
print('Indice 2:', lista[2]) #print no indice 2 da lista

# posso redefinir um valor da lista, pois ela é mutável
lista[-3] = 'Maria' #redefini o indice -3 da lista para 'Maria'
print(lista[3]) # print no indice -3 que mudou de Guilherme > Maria
