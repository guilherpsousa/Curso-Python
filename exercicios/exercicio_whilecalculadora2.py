# CALCULADORA COM WHILE TIPO 2
# A tipo 1 é mais simples, não especifica o erro, apenas diz que deu erro
# A tipo 2 eu uso not in e continue pra especificar melhor o erro caso exista

while True:
    try:
        numero1=int(input('Digite o 1o. número: '))
        if numero1 == 1111:
            print("Número secreto. Parando...")
            break

        numero2=int(input('Digite o 2o. número: '))
    except:
        print('DIGITE APENAS NÚMEROS!')
        print(30*'-')
        continue
    operacao=input('Qual a operação? (- + / *): ')
    operacaovalida='-+/*'
    
    if len(operacao) > 1:
        print('DIGITE APENAS UM OPERADOR')
        print(30*'-')
        continue
    elif operacao not in operacaovalida:
        print('DIGITE UMA OPERAÇÃO VÁLIDA')
        print(30*'-')
        continue
    elif operacao == '-':
        print(f'{numero1} - {numero2} = {numero1-numero2}')

    elif operacao == '+':
        print(f'{numero1} + {numero2} = {numero1+numero2}')

    elif operacao == '/':
        print(f'{numero1} divido por {numero2} = {numero1/numero2}')

    elif operacao == '*':
        print(f'{numero1}x{numero2} = {numero1*numero2}')

    sair=input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break