# FORMATAÇÃO DE STRINGS
# f strings -> É um recurso que permite inserir variáveis dentro de uma string.

altura = 1.83333
nome = 'Guilherme Pontes'
dinheiro = 348

# Preciso de {} para inserir a variável dentro da string, e o f antes das aspas.
print(f'Olá, meu nome é {nome} e minha altura é {altura}')

# Para números, posso usar :.2f para limitar a quantidade de casas decimais.
print(f'Olá, meu nome é {nome} e minha altura é {altura:.2f}') # Limitei a 2 casas decimais.

# Para números inteiros, posso usar :, para adicionar vírgulas como separador de milhar.
print (f'Olá, meu nome é {nome} e meu dinheiro é R$ {dinheiro:,.2f}')