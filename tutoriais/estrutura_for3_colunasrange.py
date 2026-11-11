"""  Estrutura de repetição - for + função range()
O 'for' é um iterador, automaticamente percorre elementos de uma 
sequência. E o 'range()' pode gerar a sequência numérica para 
controlar quantas vezes o loop roda.
range -> range(start, stop, step)
"""

for i in range(10): # i começa em 0 e vai chegar os if
    if i == 2: # quando i == 2, vai entrar esse if
        print('i é 2, pulando...')
        continue

    if i == 8: # quando i == 8, vai entrar nesse if
        print('i é 8, seu else não executará')
        break
# enquanto o i não entrar naqueles if acima, 
#vai pular e entrar nesse for
    for j in range(1, 3):
        print(i, j) #o print vai executar 2 vezes antes
#de voltar para o if principal, por isso faz 2 colunas
# i, j
# 0, 1
# 0, 2
else:
    print('For completo com sucesso!')
    #quando o for principal acabar, entra nesse else
