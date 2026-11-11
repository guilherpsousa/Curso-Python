# OPERADORES LÓGICOS and (e) or (ou) not (não)
'''
and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor.

or - Se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada como true/verdadeiro.

São considerados falsy 0 - 0.0 - 'str vazia' - False

not - Usado para inverter expressões (not true = false / not false = true)

none - É usado para representar um não valor
'''
print(not 1) # 1 é verdadeiro, mas 'not' o deixara falso.
print (not 0) # 0 é falso, 'not' o deixara verdadeiro.

entrada=input('[E]ntrar [S]air: ')
senha=input('Digite a senha: ')
senhacorreta = '123456'

if (entrada=='E' or entrada=='e') and senha==senhacorreta: # () pra dar preferencia no comando.
    print('Entrou')
elif entrada=='S':
    print('Sair')
elif not senha:
    print('Você não digitou a senha!')
elif senha!=senhacorreta:
    print('Senha incorreta!')

# AVALIAÇÃO DE CURTO CIRCUITO

print(True and False and 'teste') # o circuito para no primeiro valor falsy
print(0 or False or 0 or 'abc' or True) # aqui ele considera o primeiro valor verdadeiro
