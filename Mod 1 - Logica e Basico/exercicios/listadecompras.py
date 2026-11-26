lista=[]

import subprocess

while True:
    subprocess.run(["clear"], check=False)
    
    print(39*'-')
    print('_________ SELECIONE UMA OPÇÃO _________')
    opcao=input('inserir[i], apagar[a], listar[l], sair[s]: ')

    if opcao == 'i':
        item=input('Digite um nome: ')
        lista.append(item)
        print(f"Item '{item}' adcionado!.")
        input('Pressione ENTER para continuar')

    elif opcao == 'a':
        try:
            apagar=int(input('Digite o indice do item a apagar: '))
            print(f"Item '{lista[apagar]}' foi excluido!.")
            del lista[apagar]
        except IndexError:
            print('Digite um índice válido!.')
        except ValueError:
            print('Digite o número do índice!.')
        input('Pressione ENTER para continuar')

    elif opcao == 'l':
        if len(lista) > 0:
            for a, b in enumerate(lista):
                print(a, b)
        elif len(lista) == 0:
            print('A lista esta vázia!.')
        input('Pressione ENTER para continuar')

    elif opcao == 's':
        break

    else:
        print('Digite uma opção válida!')