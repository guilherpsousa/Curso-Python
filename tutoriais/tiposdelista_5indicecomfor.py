"""
Listas em Python (5- printando índice e valor com for)
    (a maneira mais facil é com o método enumerate)
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
"""
#           0       1          2
lista = ['Maria', 'Helena', 'Luiz']

''' TERMINAR A AULA '''
# ________ método com enumerate ________
for item in enumerate(lista):
    print(item)

lista.append('Gui') #adiciona o valor 'Gui' no final da lista ( 3 )
tamanho = range(len(lista)) #variavel com o tamanho da lista (0, 1, 2, 3)
for indice in tamanho: #para cada iteracao no tamanho da lista (0, 1, 2, 3)
    print(indice, lista[indice]) #print(indice da lista + o valor do indice da lista)