"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

digito=int(input('Digite um digito: '))
novodigito = digito if digito <= 9 else 0
print(novodigito)