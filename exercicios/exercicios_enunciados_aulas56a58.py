"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
""" 
numero = input('Digite um número inteiro: ')
try:
    numerointeiro = int(numero)
    if numerointeiro%2==0:
        print(f'O número {numerointeiro} é PAR')
    else:
        print(f'O número {numerointeiro} é IMPAR')

except:
    print(f'{numero} - Não é um número inteiro')

 """

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
""" 
horario=input('Digite a hora [XX:XX]: ')

try:
    hora = int(horario) # variavel nova pro try aceitar apenas numeros int. 
    if (horario>='00:00') and (horario<='11:59'):
        print(f'Bom dia, agora são {horario} horas')
    elif (horario>='12:00') and (horario<='17:59'):
        print(f'Boa tarde, agora são {horario} horas')
    elif (horario>='18:00') and (horario<='23:59'):
            print(f'Boa noite, agora são {horario} horas') 

except:
    print('Digite um horário válido!.')

 """

""" Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".  """
"""  
nome=input('Digite seu primeiro nome: ')

if len(nome) >= 2 and len(nome) <= 4:
    print('Nome curto')
elif len(nome) >=5 and len(nome) <=6:
    print('Seu nome é normal')
elif len(nome)>6:
    print('Seu nome é muito grande')
else:
    print('Digite um nome válido')
 """
