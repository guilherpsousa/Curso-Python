""" Listas em Python (3- append, insert)
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

# _____ adcionando valores com .append() _____

lista=[10, 20, 30, 40]
lista.append('Gui')
print('Lista com valor adcionado:', lista)

# _____ inserindo valores com 'insert' _____
# o () do insert, é sempre (indice, valor a inserir)

#       0     1   2   3    4
lista=['Gui', 10, 20, 30, 40]
lista.insert(1, 'Pontes')
print(lista)

# posso adcionar no ultimo indice usando
lista=['Gui', 10, 20, 30, 40]
lista.insert(5, 'Pontes')
print(lista)

# OU POSSO simplesmente usar o .append (Feito pra isso)
lista=['Gui', 10, 20, 30, 40]
lista.append('Pontes')
print(lista)