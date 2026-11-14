"""
5. Lista básica
Crie uma lista vazia e use um while para pedir nomes ao usuário até ele digitar sair. No final:

mostre quantos nomes foram digitados (len);
mostre cada nome com for;
mostre o primeiro e o último nome (lista[0] e lista[-1]).
"""
lista=[]
while True:
    nomes=input("Digite um nome. Ou digite 'sair' para parar: ")
    if nomes == 'sair':
        print(f'Você digitou {len(lista)} nomes')
        for iteracao in lista:
            print(iteracao)
        print(f'Primeiro nome: {lista[0]}. Ultimo nome: {lista[-1]}')
        break
    lista.append(nomes)
