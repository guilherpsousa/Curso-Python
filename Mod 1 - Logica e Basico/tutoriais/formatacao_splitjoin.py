""" split e join com list e str
split > divide uma string
join > une uma string
str, listas e tuplas são iteraveis, podem ser convertidos entre si usando split e join
"""

#caso () esteja vazio, ele vai dividir a string em cada espaço
frase="Olha só que, coisa interessante" 
lista_frases=frase.split() 
print(lista_frases)

#caso () esteja vazio, ele vai unir a string em cada espaço
frases_unidas = '*'.join(lista_frases) 
print(frases_unidas)

nova_frase='  tambem posso usar .strip para remover espaços     '
print(nova_frase.strip()) # strip remove espaços dos dois cantos,
                        #rstrip remove espaços da direita
                        #lstrip remove espaços da esquerda