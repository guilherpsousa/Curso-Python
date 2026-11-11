# Input, funciona como o "Leia" do portugol.
# A diferença é que a pergunta, a váriavel e a função "input/leia" ficam na mesma linha.

nome = input('Qual seu nome?: ') # Por padrão, input recebe str
print(f'Seu nome é {nome}')

# Tambem posso usar o sinal de = após chamar a váriavel.
print(f'Seu nome é {nome=}') # Assim o print manda "nome+valor da váriavel."

# Pra eu transformar a váriavel str em uma váriavel de números eu posso fazer de 2 maneiras

# 1. Convertendo a str para int na mesma linha do input
# numero_1 = int(input('Digite um número: '))

# 2. Jogando oque eu receber da váriavel str para outra váriavel formatada em int
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos dois números é: {int_numero_1+int_numero_2}')


"""
No "1." se eu digitasse uma letra em um input(int) ele quebraria no começo.
No "2." se eu digitasse uma letra ele aceitaria>checaria>e depois quebraria.
"""
