'''
criar uma variavel com meu nome
fazer com que cada vez que passar pelo while, escreva(print) uma letra até a ultima
DICAS
print(variavel[2]) # sem : ele pega apenas o caractere do indice indicado
print(len(variavel)) # indice começa no 0, mas 'len' conta o total de caracteres
'''

""" 
nome='Guilherme'
compnome=len(nome) #9

inicio=0
indice=0
while inicio <= compnome:
    if inicio==compnome:
            break
    print(f'{nome[indice]}')
    inicio+=1
    indice+=1
"""

#     012345678
nome='Guilherme'
nova_str=''

inicio=0
while inicio <= 8:
    nova_str+='*' + nome[inicio]
    inicio+=1
print(nova_str)
