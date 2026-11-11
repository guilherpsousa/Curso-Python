''' while PT 1 - break e operadores de atribuição
PT2 'continue'
PT3 'while dentro de while com colunas'
PT4 'while / else'

executa uma ação enquanto uma condição for verdadeira
Começo com 'while' e termino com 'break'
Em caso de loop infinito, teclas ctrl+c no terminal
Operadores de Atribuição: = += -= /= //= **= %=
    ex: += Soma o valor à variável atual e guarda o resultado nela mesma
        -= Subtrai o valor da variável atual e guarda o resultado nela mesma
'''

condicao=True
while condicao:
    nome=input('Digite seu nome: ')
    print(f'Seu nome é {nome}')
    if nome=='sair': #usando if sair como escape pra parar o programa
        break

print(40*'-')


contador=0
contagem = int(input('Contar até qual número?: '))
    #se eu não usar int no input, minha variavel contagem recebe uma str, e...
    #assim não consegue executar a while contador(int) < contagem(str)

while contador < contagem:
    contador=contador+1
    #tambem poderia usar 'contador+=1' ao inves de 'contador=contador+1'
    print(contador)

print('ACABOU')

#while é mais usado quando não se sabe o número de repetições, 
#ou seja, quando não se sabe a quantidade de vezes que o 
#bloco de código será executado.