operacaovalida='+-/*'

while True:
    try:
        numero1=float(input('Digite o 1º número: '))
        numero2=float(input('Digite o 2º número: '))
    except:
        print('ERRO: Digite apenas números!')
        continue

    operacao=input('Digite uma operação [+ - / *]: ')
    if operacao not in operacaovalida:
        print('ERRO: Digite uma operação válida! [+ - / *]')
        continue
    if len(operacao) != 1:
        print('ERRO: Digite apenas uma operação!')
        continue     

    if operacao == '+':
        print(f'{numero1}+{numero2} = {numero1 + numero2} ')
    if operacao == '-':
        print(f'{numero1}-{numero2} = {numero1 - numero2} ')
    if operacao == '/':
        print(f'{numero1}/{numero2} = {numero1 / numero2} ')
    if operacao == '*':
        print(f'{numero1}*{numero2} = {numero1 * numero2} ')

    stop=input('Quer continuar? [s/n]: ').lower()
    if stop == 'n':
        break
    
    