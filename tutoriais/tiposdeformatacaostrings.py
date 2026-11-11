# VÁRIAVEIS PARA PARÂMETROS DAS EXPLICAÇÕES
altura = 1.83333
nome = 'Guilherme Pontes'
dinheiro = 348768

### RESUMO DE CADA TIPO DE FORMATAÇÃO ###

# FORMATAÇÃO DE STRINGS - [mais facil, e mais recente]
# f strings -> É um recurso que permite inserir variáveis dentro de uma string.
# Preciso de {} para inserir a variável dentro da string, e o f antes das aspas.
print(f'Olá, meu nome é {nome} e minha altura é {altura}')
# Para números, posso usar :.2f para limitar a quantidade de casas decimais.
print(f'Olá, meu nome é {nome} e minha altura é {altura:.2f}') # Limitei a 2 casas decimais.
# Para números inteiros, posso usar :, para adicionar vírgulas como separador de milhar.
print (f'Olá, meu nome é {nome} e meu dinheiro é R$ {dinheiro:,.2f}')

print(40*'-')

# FORMATAÇÃO COM format() eu posso usar indices para chamar váriaveis.
# A {} serve para chamar a variável que quero inserir na string.
# Apenas usando as {} sem indice, a ordem das variaveis sera a ordem que eu chamei na função format
string = 'Altura: {:.2f} Nome: {} R${:.2f}' # formatei a variavel 'altura e dinheiro' com :.2f
formato = string.format(altura, nome, dinheiro)
print(formato)

# Para eu chamar na ordem que eu quiser, eu uso o número correspondente ao indice criado.
string = 'Nome: {0} Dinheiro: {1:,.2f} Altura: {2:.2f}'
formato = string.format(nome, dinheiro, altura) # indice 'nome > 0' - 'dinheiro > 1' - 'altura > 2'
print(formato)

print(40*'-')

# FORMATAÇÃO COM INTERPOLAÇÃO
""" 
Eu chamo essa formatação usando % e a letra correspondente ao tipo da váriavel
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
hexadecimal é o código de números formado por letras de A até F e numeros de 0 a 9 
"""
variavelinterpolacao = '%s, o preco é R$%.2f' % (nome, dinheiro) # entre () caso eu chame mais de 1 variavel
print(variavelinterpolacao)
print('O hexadecimal de %d é %X' % (198, 198)) # não usei variaveis como parâmetros