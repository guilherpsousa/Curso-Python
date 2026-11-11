"""
FATIAMENTO DE STRINGS

 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
i= inicio   f= fim     p= passo
len: retorna a qtd total de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[2]) # sem : ele pega apenas o caractere do indice indicado
print(variavel[4:]) # [inicio no 4 caractere e : pra ir até o final]
print(variavel[4:6]) # [inicio no 4 caractere e : final no 6] 
print(variavel[-9:-6]) # [usando indice negativo] 
print('ABCDEFGHIJKLM'[0:20:2]) # [inicio:final:pula de 2 em 2]
print('OLA MUNDO'[::-1]) # [ :: ignoro inicio e final, coloco só o passo -1 invertido]
print(len(variavel)) # indice começa no 0, mas 'len' conta o total de caracteres