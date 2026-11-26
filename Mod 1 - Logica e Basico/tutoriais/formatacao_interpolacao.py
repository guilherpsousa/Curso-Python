'''
Formatação básica do tipo INTERPOLAÇÃO
Eu chamo essa formatação usando % e a letra correspondente ao tipo da váriavel 
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
hexadecimal é o código de números formado por letras de A até F e numeros de 0 a 9

'''
#EXEMPLO

nome = 'Gui'
preco = 1298.108

variavelinterpolacao = '%s, o preco é R$%.2f' % (nome, preco) # entre () caso eu chame mais de 1 variavel
print(variavelinterpolacao)
print('O hexadecimal de %d é %X' % (198, 198)) # não usei variaveis como parâmetros

variavelfstrings = (f'{nome}, o preço é R${preco:.2f}') # relembrando variavel com f'strings
print(variavelfstrings)
