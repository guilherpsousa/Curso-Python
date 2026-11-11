''' while PT 4 - while / else #recurso raramente usada
PT1 'break e operadores de atribuição'
PT2 'continue'
PT3 'laços / while dentro de while com colunas'

Estrutura de REPETIÇÃO - while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Em caso de loop infinito, teclas ctrl+c no terminal
Operadores de Atribuição: = += -= /= //= **= %=
# continue faz com que eu possa pular algo e depois continuar, ao inves de parar(break) 
'''

string='Valor qualquer'
i=0

#while execute se o indice for < que len(string)
while i < len(string):
    letra=string[i]

    if letra==' ':
        break

    print(letra)
    i+=1
else: #o else geralmente sempre existe no final do while, mesmo sem digitar
    print('Não encontrei um espaço na string')

print('Fora do while')

#while é mais usado quando não se sabe o número de repetições, 
#ou seja, quando não se sabe a quantidade de vezes que o 
#bloco de código será executado.