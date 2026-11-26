"""
3. range: contagem personalizada
Peça um número inicial, um final e um passo. Mostre todos os números nesse intervalo 
usando range(inicio, fim, passo).
Exemplo: início 0, fim 20, passo 5 mostra 0, 5, 10, 15.
"""

print('Me de 3 números, sendo eles (inicio> fim> passo)')
print(20*'-')
numero1=int(input('Digite o 1º número: '))
numero2=int(input('Digite o 2º número: '))
numero3=int(input('Digite o 3º número: '))
print(20*'-')
print(f'Inicio: {numero1}. Fim: {numero2}. Passo: {numero3}.')
numerostotal=''
for iteracao in range(numero1, numero2+1, numero3):
    numerostotal+=f"{iteracao}, "

print(numerostotal)
