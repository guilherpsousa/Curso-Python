# CALCULADORA COM WHILE
# A tipo 1 é mais simples, não especifica o erro, apenas diz que deu erro
# A tipo 2 eu uso not in e continue pra especificar melhor o erro caso exista

while True:
    try:
        numero1=int(input('Digite o 1o. número: '))
        numero2=int(input('Digite o 2o. número: '))
        operacao=input('Qual a operação? (- + / *): ')
        operacaovalida='-+/*'

        if operacaovalida > 1:
            print('Digite apenas um operador')
            continue
        elif operacao not in operacaovalida:
            print('Digite uma operação valida')
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
    except:
        print('Digite em sequencia quando pedido número 1 > número 2 > operador (- + / *)')