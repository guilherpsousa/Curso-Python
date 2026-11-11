# Tipos de conversões em python, basicamente é a mudança de um tipo de dado para outro.
# Aqui para ter coerencia na conversão, é necessário que o dado 1 seja compatível com o dado 2.
print(1+1) # int + int = int
print(1+1.5) # int + float = float

# Para converter um tipo de dado para outro, posso usar a função "str()" ou "float()".
print(str(11)+'b') # o número 11 foi convertido para string, e agora é possível.

# Sem transformar o tipo de dado 1 para que fique igual o dado 2 fica impossivel a operação.
print('1'+1) # str + int = TypeError (não é possível converter str para int)
