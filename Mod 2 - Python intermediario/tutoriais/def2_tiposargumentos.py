"""
Argumentos nomeados e não nomeados em funções
Argumento nomeado tem nome com sinal de igual 
Argumento não nomeado recebe apenas o argumento (valor)
"""

def pessoa(a, b):
    print(f'Olá {a}, você tem {b} anos')


pessoa('Gui', 26) #argumento não nomeado, chamará a função na ordem
pessoa(b=26, a='Gui') #argumento nomeado eu posso passar a ordem
# b, a = parâmetros | 26, Gui = argumentos