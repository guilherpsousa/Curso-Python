"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

#é mais inteligente usar para um não valor o "None", doque o "0"
    #pois 0 representa False, e None representa um não valor

def soma(x, y, z=None):
    if z is None: # se z for um não valor
        print("Z não tem valor definido =", z)
        
    else: # contrario disso / z tem valor
        print("Z tem um valor definido =", z)
        print(f'{x=} + {y=} + {z=} = {x+y+z}')

soma(1, 2, 3) #chamando a função sem nomear os arumentos

print(20*'-')

soma(z=None, x=6, y=4) #função nomeando os argumentos