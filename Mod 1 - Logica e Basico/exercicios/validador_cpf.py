import re
import sys

print("_____ VÁLIDADOR DE CPF _____")

cpf = input("DIGITE SEU CPF: ")
cpfformatado = re.sub(r'[^0-9]', '', cpf)
if len(cpfformatado) != 11:
    print('Seu CPF deve conter 11 dígitos!.')
    print(28*'-')
    sys.exit()

cpfsequencial=cpfformatado==cpfformatado[0]*len(cpfformatado)
if cpfsequencial:
    print("Você digitou dados sequenciais!.")
    print(28*'-')
    sys.exit()

# bloco para checar o primeiro dos últimos 2 digitos
contador_regressivo1=10
novedigitos=cpfformatado[0:9]
resultado1=0
for iteracao in novedigitos:
    resultado1+=int(iteracao)*contador_regressivo1
    contador_regressivo1+=-1
resultado1=(resultado1*10)%11
resultado1=0 if resultado1 > 9 else resultado1
# bloco para checar o segundo dos últimos 2 digitos
contador_regressivo2=11
dezdigitos=novedigitos+str(resultado1)
resultado2=0
for iteracao in dezdigitos:
    resultado2+=int(iteracao)*contador_regressivo2
    contador_regressivo2+=-1
resultado2=(resultado2*10)%11
resultado2=0 if resultado2 > 9 else resultado2

novocpf=f'{novedigitos}{resultado1}{resultado2}'

if novocpf == cpfformatado:
    print(f'> O CPF {novocpf}, é válido!')
    print(28*'-')

else:
    print('> CPF inválido!')
    print(28*'-')