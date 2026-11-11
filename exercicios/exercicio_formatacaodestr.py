nome=(input('Digite seu nome: '))
idade=(input('Idade: '))
if '' in nome and idade: # poderia ter sido 'if nome and idade:'
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]} ')
else:
    print('Você não digitou seu nome ou sua idade.')