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
plsecreta='amor'
letras_acertadas=''
tentativas=0

print(f'A palavra secreta tem {len(plsecreta)} letras1)')

while True:
    letra=input('Digite uma letra: ').lower()
    if letra == ' ':
        print('Digite uma letra!, espaço não é permitido!')
        continue 
    if len(letra) != 1: 
        print('Digite apenas uma letra!')
        continue
        
    if letra in plsecreta:
        letras_acertadas+=letra

    palavraformada=''
    for iteracao in plsecreta:
        if iteracao in letras_acertadas:
            palavraformada+=iteracao
        else:
            palavraformada += '*'
    print(palavraformada)
    tentativas+=1
    if palavraformada == plsecreta:
        print('Parábens, você acertou a palavra secreta')
        print(f'Quantidade de tentativas: {tentativas}')
        break
        
