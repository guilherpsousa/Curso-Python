""" Listas em Python (2- del, pop, clear)
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido e o guarda
    del - apaga um valor do índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#RESUMO del = apenas apaga um valor
#       pop = guarda o valor com ele e o apaga

# _____ apagando um valor com del _____

lista=[10, 20, 30, 40]
del lista[0] # OU posso usar [-1] pra deletar o ULTIMO valor da lista
print(lista)

# _____ apagando a lista inteira com .clear() ____

lista=[10, 20, 30, 40]
lista.clear()
print(lista)

# _____ removendo valores com .pop() _____

#removendo o ultimo valor da lista com .pop
lista=[10, 20, 30, 40]
print(lista.pop()) #removi e dei print (ao mesmo tempo) no ultimo valor da lista (40)

#removendo um valor usando indice
#      0   1   2   3
lista=[10, 20, 30, 40]
lista.pop(2) #caso eu não use o indice dentro de (), ele apaga e guarda o ultimo valor da lista
print(lista)

# _____ removendo e adcionando um valor a uma variavel _____

lista=[10, 20, 30, 40]
nova_variavel=lista.pop(2) 
    #removi da lista o valor do indice 2 e o coloquei em uma nova variavel
print(lista,'foi removido o:', nova_variavel)  

# OU caso eu não queira guardar em uma váriavel, só apagar e retornar
lista=[10, 20, 30, 40]
print(lista,'foi removido o:', lista.pop(2))  
