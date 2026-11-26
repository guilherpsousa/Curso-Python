'''
SITE COM CÓDIGOS/FUNÇÕES/MACETES PYTHON
https://docs.python.org/pt-br/3/builtins/stdtypes.html
Imutáveis que vimos até agora, aula 54: str, int, float, bool

exemplo:
    nome='Guilherme'    eu não consigo alterar o valor dessa variavel, então ela é imutavel
    idade=26    eu não consigo alterar o valor int dessa váriavel, ela tambem é imutavel.
# no maximo oque eu consigo é fatiar, adcionar letras, colocar em maisculo/minusculo
através de funções, mas o valor da váriavel continuara o mesmo.

'''
string = 'Guilherme' #exemplos de fatiamento abaixo.
print(string[2]) # sem : ele pega apenas o caractere do indice indicado
print(string[4:]) # [inicio no 4 caractere e : pra ir até o final]
print(string[0:2]) # [inicio no 4 caractere : final 6 caractere] 
print('ABCDEFGHIJKLM'[::2]) # [inicio:final:pula de 2 em 2 (passo)]