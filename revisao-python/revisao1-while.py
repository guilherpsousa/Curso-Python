"""
while: adivinhe o número
O programa escolhe um número secreto (por exemplo, 7). 
Use while para pedir palpites até o usuário acertar. 
A cada erro, diga se o palpite foi “maior” ou “menor” que o número secreto. 
No final, mostre em quantas tentativas ele acertou.
"""

numsecreto=36
tentativas=1
print('________ADIVINHE O NÚMERO________')
while True:
    numtalvez=int(input('Digite um número: '))
    if numtalvez==numsecreto:
        print(f'Parabéns, você acerto o número secreto!!! ({numsecreto})')
        print(f'Você acertou com {tentativas} tentativas.')
        break
    if numtalvez > numsecreto:
        print('Seu número é maior')
    elif numtalvez < numsecreto:
        print('Seu número é menor')
    tentativas+=1
    