''' while PT 3 - laços / while dentro de while com colunas
PT1 'break e operadores de atribuição'
PT2 'continue'
PT3 'while / else'

Estrutura de REPETIÇÃO - while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Em caso de loop infinito, teclas ctrl+c no terminal
Operadores de Atribuição: = += -= /= //= **= %=
# continue faz com que eu possa pular algo e depois continuar, ao inves de parar(break) 
'''

qtd_linhas=5
qtd_colunas=5

linha=1
while linha <= qtd_linhas:
    coluna=1
    while coluna <= qtd_colunas: #esse while se repete 5 vezes, antes de ir pro while maior
        print(f'{linha=} {coluna=}') #nesse print mostra uma variavel do lado da outra
        coluna+=1 #só sai desse while quando coluna atingir <= qtd_colunas
                  #while menor se repete 5 vezes por causa da while maior
    linha+=1

print('Acabou')

#while é mais usado quando não se sabe o número de repetições, 
#ou seja, quando não se sabe a quantidade de vezes que o 
#bloco de código será executado.