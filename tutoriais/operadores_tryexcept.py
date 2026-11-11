'''
INTRODUÇÃO AO TRY/EXCEPT
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
# em 'try:' o código vai funcionar até onde ele der erro...
# quando der erro, ao inves de mostrar mensagem de erro, ele executa o bloco em 'except:'
numero_str = input(
    'Digite um numero pra dobrar: '
)
try:
    numero_float = float(numero_str)
    print(f'{numero_float*2:.2f}')
except:
     print('Isso não é um número')

# TAMBEM CONSIGO EXECUTAR DESSA MANEIRA: 
# o '.isdigit():' faz com que o if só execute caso o valor recebido em numero_str seja um digito

""" 
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'{numero_float*2:.2f}')
else:
    print('Isso não é um número') 
"""