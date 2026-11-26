frase='O Python é uma linguagem de programação'\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes=0
letra_apareceu_mais_vezes=''

while i < len(frase):

    if frase[i] == ' ': #bloco if pra pular o espaço em branco
        i+=1
        continue
    
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes=letra_atual

    i+=1

print(
    f'A letra que apareceu mais vezes foi "{letra_apareceu_mais_vezes}". '
    f'E apareceu {qtd_apareceu_mais_vezes} vezes.'
)
