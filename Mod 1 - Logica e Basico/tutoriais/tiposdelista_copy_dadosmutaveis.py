"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria']
lista_b = lista_a #assim estou puxando o valor da lista_a para a lista_b
lista_c = lista_a.copy() #assim estou copiando o valor da lista_a para a lista_c

print('Lista b:', lista_b)
print('Lista c:', lista_c)