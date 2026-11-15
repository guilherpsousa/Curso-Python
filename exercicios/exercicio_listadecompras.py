"""
Faça uma lsta de compras com listas
O usuario deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices na lista
"""

lista=[]
listaenumerada=list(enumerate(lista))

while True:
    # for a, b in enumerate(lista):
    #     print(a, b)
    
    print(39*'-')
    print('_________ SELECIONE UMA OPÇÃO _________')
    opcao=input('inserir[i], apagar[a], listar[l], sair[s]: ')

    if opcao == 'i':
        item=input('Digite um nome: ')
        lista.append(item)
        print(f"Item '{item}' adcionado!.")

    elif opcao == 'a':
        try:
            apagar=int(input('Digite o indice do item a apagar: '))
            print(f"Item '{lista[apagar]}' foi excluido!.")
            del lista[apagar]
        except IndexError:
            print('Digite um índice válido!.')
        except ValueError:
            print('Digite o número do índice!.')

    elif opcao == 'l':
        if len(lista) > 0:
            for a, b in enumerate(lista):
                print(a, b)
        elif len(lista) == 0:
            print('A lista esta vázia!.')

    elif opcao == 's':
        break

    else:
        print('Digite uma opção válida!')