# A função format() é usada para inserir variáveis dentro de uma string e tambem formatar váriaveis.
# A {} serve para chamar a variável que quero inserir na string.

a = 'A'
b = 'B'
c = 1.1

# Apenas usando as {} sem indice, a ordem das variaveis sera a ordem que eu chamei na função format
string = 'TESTEA={} TESTEB={} TESTEC{:.2f}' # formatei a variavel 'c' com :.2f
formato = string.format(a, b, c)

# Para eu chamar na ordem que eu quiser, posso usar {0}, {1}, {2}. OBS: A contagem começa do 0.
string = 'TESTEA={1} TESTEB={0} TESTEC{2:.2f}'

# Posso nomear parâmetros para chamalos pelo nome ao inves de chama-los por indice.
string = 'TESTEA={nome1} TESTEB={nome2} TESTEC{nome3:.2f}' 
formato = string.format(nome1=a, nome2=b, nome3=c)


print(formato) # Estou chamando a váriavel formato, váriavel essa que chama a váriavel string.