''' COMO O 'for' FUNCIONA por de baixo dos panos.

Iterável -> algo que pode me entregar 1 caractere por vez
    str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entrega o próximo valor do iterador
Iter -> me entrega seu iterador
'''

#___iter___()
texto = iter('Gui') #transformei a variável texto em um iteravel
#se eu não transformar a variável em um iteravel, o next não vai funcionar
print(next(texto)) #estou chamando 1 valor do iterador por vez
print(next(texto))
print(next(texto))

#se eu chamar mais um next, vai estourar a qnt de 
#caracteres e vai gerar um erro
""" 
o for não deixa estourar a quantidade de caracteres, ele só
vai usar oque tem disponível, e quando acabar ele para sozinho.
"""