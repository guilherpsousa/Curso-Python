# Essas funções básicas de strings funcionam melhor com f'strings e format()
'''
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda (puxa a variavel pra direita e completa para a ESQUERDA)
< - Direita (puxa a variavel pra esquerda e completa para a DIREITA)
^ - Centro
Sinal - + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'TESTE'
print(f'{variavel}')
print(f'{variavel:A>3}') #nada aparece pois 'TESTE' tem mais de 3 caracteres.
print(f'{variavel:B>8}') #puxa a variavel pra direita e completa para a ESQUERDA
print(f'{variavel:0<8}') #puxa a variavel pra esquerda e completa para a DIREITA
print(f'{variavel:0^8}') #deixa a variavel no centro e completa nos cantos
print(f'{1000506.14768:+,.1f}') #com + após :, eu quero que o + apareça caso o número seja positivo
print(f'O hexadecimal de 1500 é {1500:05X}') # :05X seria "preencher com 0, até 5 caracteres o valor decimal de 1500"
