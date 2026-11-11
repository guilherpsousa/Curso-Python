"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

plsecreta='bruna'
tentativas=0
letrasacertadas=''
erros=0

print(f'A palavra secreta tem {len(plsecreta)} letras')
while True:
    letra=input('Digite uma letra: ').lower()
    if letra == ' ':
        print('Espaço não vale! ')
        continue
    if len(letra) != 1:
        print('Digite uma letra! ')
        continue
    if letra not in plsecreta:
        erros+=1
        print(f'Letra incorreta. Total de erros {erros}/20')
        tentativas+=1
        continue
    if letra in letrasacertadas:
        print('Você já digitou essa letra! ')
        tentativas+=1
        continue
    if letra in plsecreta:
        letrasacertadas+=letra
        tentativas+=1

    palavraformada=''
    for iteracao in plsecreta:
        if iteracao in letrasacertadas:
            palavraformada+=iteracao
        else:
            palavraformada+='*'

    if palavraformada==plsecreta:
        break
    print(palavraformada)

print(f"Parabéns, a palavra formada era '{plsecreta}'")
print('Erros:', erros)
print('Tentativas:', tentativas)

