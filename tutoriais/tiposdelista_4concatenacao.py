""" Listas em Python (4- extend, concatenar)
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#Método 1 para juntar listas - usando o operador +
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #junta as duas listas em uma nova variável
print(lista_c)

#Método 2 para juntar listas - usando o método extend
lista_a.extend(lista_b) #junta a lista_b na lista_a (mexe apenas na lista_a)
print(lista_a)