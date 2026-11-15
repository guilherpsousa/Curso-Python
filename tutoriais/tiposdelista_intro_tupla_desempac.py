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