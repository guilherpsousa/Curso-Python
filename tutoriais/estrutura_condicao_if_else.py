"""
if / elif / else
se / senão se / senão

Posso usar vários "elif" no código.
"""
entrada=input('Você quer "entrar" ou "sair" do sistema?: ')

if entrada=='entrar':
    print('Você entrou no sistema')
elif  entrada=='sair':  
    print('Você saiu do sistema')
elif entrada=='seila':
    print('Voce digitou "seila"')
else:
    print('OPÇÃO INCORRETA')

print('BLOCO DE CIMA EXECUTADO')