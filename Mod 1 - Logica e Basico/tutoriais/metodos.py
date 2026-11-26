#__________________MÉTODOS_________________

#lower, startswith, endswith_______________
#upper deixa tudo em maiúsculo
nome=input('Digite seu nome: ').lower().startswith('g')
print(nome) #assim 'print' vai me retornar bool, pois a variavel nome se tornou boolean

nome=input('Digite seu nome: ').lower()
print(nome) #esse print vai me retornar minha resposta toda em minusculo
print(nome.startswith('g')) #esse print vai me retornar um bool
#startswith('g') = nome começa com 'g'?
print(nome.endswith('e'))
#endswith('e') = nome termina com 'e'?

print(30*'-')

#count _____________________________________
frase='O Python é uma linguagem de programação'\
    'multiparadigma.'\
    'Python foi criado por Guido van Rossum.' #posso usar .lower() para deixar tudo minusculo
print(frase.count('Python')) #quantas vezes a palavra 'Python' aparece na frase 