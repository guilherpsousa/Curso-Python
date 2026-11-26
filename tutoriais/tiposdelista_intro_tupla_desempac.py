"""
Tipo tupla - Uma lista imutável
Basta removar os [] dos valores da lista, assim ela fica imutavel
    ex: não fica possivel alterar valores dentro dela
Ainda consigo acessar valores com indice
"""

nomes = 'Maria', 'Helena', 'Luiz'
print(nomes[1])

print(30*'-')

"""
Introdução ao empacotamento e desempacotamento
Posso empacotar e desempacotar valores em listas.
"""

# Dessa maneira o py associa cada variavel com 1 valor dentro da lista
#   OBS: Lista e variavel deve ter a mesma quantidade para associar.
carro1, carro2, carro3=['volks', 'chev', 'fiat']
print(carro3)

# Usando '*' eu digo pro py algo como 'resto', para assim incluir todas as váriaveis
carro1, *_=['volks', 'chev', 'fiat']
print(carro1)

print(30*'-')

""" Desempacotamento em chamadas (métodos e funções) """

lista=['Gui', 'Maria', 'Dani', 'Pedro', 'Gu']
print(lista)
print(*lista, sep=', ', end='. \n') # \n para pular linha
#no print, o uso do * desempacota os itens e entrega um separado do outro
#sep= determina como cada item é separado, alem de colocar tudo na mesma linha.
#end= determina como o print termina

for item in lista:
    print(item, end=', ') #com for eu chamo a , no final(end) de cada item
                        #mas com isso tambem não consigo colocar . depois do ultimo item
                        #por isso o jeito mais fácil é desempacotar direto no print(*lista)