# Tipos de números em python, inteiro e decimal/real/números quebrados.
# Números inteiros são "int", já números decimais são "float".
print(10) # int
print(10.5) # float

# Type mostra o tipo de dado que esta dentro da variável.
print(type(10)) # Nesse caso INT
print(type(10.5)) # Nesse caso FLOAT

# Do mesmo jeito, Type funciona com strings.
print(type("Hello, world!")) # Nesse caso str

numero1 = 0.1
numero2 = 0.7
numero3 = numero1 + numero2

print(numero3) # O resultado não é 0.8, mas sim 0.799999999999

# eu posso contornar esse problema usando a função round, que arredonda o número quebrado.
print(round(numero3, 2)) 

# ou posso formatar o número quebrado usando f-string, que também arredonda o número quebrado.
print(f"{numero3:.2f}") 