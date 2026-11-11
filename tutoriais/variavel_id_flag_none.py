"""
Flag (bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
É uma alternativa ao debugger, desse modo eu consigo saber por onde o código esta passando.
"""

condicao = True # True ou False
passou_no_if = None # passou_no_if = none (não tem valor)

if condicao: # se a condição for verdadeira, o código passa no if
    passou_no_if = True # se verdadeira, passou_no_if passa a ser True
    print('PASSOU NO IF')
else: # se a condição for o contrário (else), passará por aqui
    passou_no_if = False # se verdadeira, passou_no_if passa a ser False
    print('NÃO PASSOU NO IF')

print(passou_no_if) # vai me escrever se ela passou (True) ou não passou (False) no if.

#################################################################
print(30*'-')
print('ABAIXO EXPLICA ID')

""" ID() python inteligente, ele usa a mesma memória caso oque está guardado na 
váriavel seja exatamente igual a outra váriavel. """
v1 = 'a' # a minusculo
v2 = 'A' # A maisculo
print(id(v1))
print(id(v2))