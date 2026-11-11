# Testando se o primeiro valor é maior ou menor que o segundo.

primeirovalor=input('Digite o primeiro valor: ')
segundovalor=input('Digite o segundo valor:')

if primeirovalor>segundovalor:
    print(f'O {primeirovalor=} é maior do que o {segundovalor=}')
elif primeirovalor<segundovalor:
    print(f'O {segundovalor=} é maior do que o {primeirovalor=}')
elif primeirovalor==segundovalor:
    print(f' Os valores {primeirovalor=} e {segundovalor=} são iguais')

        