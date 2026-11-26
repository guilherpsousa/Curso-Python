"""  Estrutura de repetição - for + função range()
O 'for' é um iterador, automaticamente percorre elementos de uma 
sequência. E o 'range()' pode gerar a sequência numérica para 
controlar quantas vezes o loop roda.
range -> range(start, stop, step)
"""

'FOR' #for é um iterador, ele quando parar, não precisa de contador

texto='Python'
nova_for =''

for letra in texto: 
    nova_for += f'*{letra}'
print(nova_for)

# com while o código seria maior, pois eu precisaria 
# de um contador, pra saber quando parar
texto='Python'
contador=0
nova_while=''
while contador < len(texto):
    nova_while += '*' + texto[contador]
    contador+=1
print(nova_while)

'________________________FOR + RANGE(start, stop, step)________________________'


numeros = range(10) #gera uma variavel com os números de 0 a 9

print(numeros[2])
print('fim')

for iteracao in range(10): #sequência de 0 a 9
    print(iteracao) #imprime os números de 0 a 9
print('fim')

for iteracao in range(1, 10): #sequência de 1 a 9
    print(iteracao)
print('fim')

for iteracao in range(1, 10, 2): #sequência de 1 a 9, pulando de 2 em 2
    print(iteracao)
print('fim')

            #range(start , stop , step)
for iteracao in range(10, 0 , -1): #sequência 10 a 1, step negativo
    print(iteracao)
print('fim')
