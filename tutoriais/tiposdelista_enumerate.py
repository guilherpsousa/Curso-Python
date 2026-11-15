""" Consigo enumerar listas 
enumerate - enumera iteráveis (índices)
"""

#           0       1        2
lista = ['Gui', 'Helena', 'Luiz']
lista.append('João')
#posso usar a o metodo start=1 pra começar a lista do numero 1 (ou do que eu quiser)
# Ex: listaenumerada=list(enumerate(lista, start=1))

''' ______ usando o iterador enumerate. maneira 1 ______'''
#se eu criar uma nova variavel pra receber a lista enumerada, eu preciso transforma-la em list

listaenumerada=list(enumerate(lista)) #criei uma variavel pra isso e usei list()
# for item in listaenumerada:
#     print(item)
print(listaenumerada[1]) #convertendo a variavel em list, eu consigo usar print direto
    #consigo usar indice   

print(20*'-')
'''______ usando o iterador enumerate com for. maneira 2 ______'''

for item in enumerate(lista): #sem usar nova variavel
    print(item)

print(20*'-')
'''______ usando o iterador enumerate com for. maneira 3 ______'''

# por causa do enumerate a lista não é mais só os nomes, ela tem os indices tambem!
# então para cada item que é 'a'0, 'b'Gui, 'a'1, 'b'Helena, 'a'2, 'b'Luiz, 'a'3, 'b'João

for a, b in enumerate(lista):
    print(a, b) #a cada loop vai printar a, b até acabar a lista