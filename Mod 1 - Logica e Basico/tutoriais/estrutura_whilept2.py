''' while PT 2 - continue
PT1 'break e operadores de atribuição'
PT3 'while dentro de while com colunas'
PT4 'while / else'

Estrutura de REPETIÇÃO - while(enquanto)
executa uma ação enquanto uma condição for verdadeira
Em caso de loop infinito, teclas ctrl+c no terminal
Operadores de Atribuição: = += -= /= //= **= %=
# continue faz com que eu possa pular algo e depois continuar, ao inves de parar(break) 
'''

contador = 0

while contador < 100: # contador vai contar até 100
    contador += 1
    if contador == 38:
        continue  # pula o print quando for 38 e continua o que faltou
    print(contador)
    if contador==40: # vai repetir o while até aqui, e quando for 40 vai entrar no if>break
        break

#while é mais usado quando não se sabe o número de repetições, 
#ou seja, quando não se sabe a quantidade de vezes que o 
#bloco de código será executado.