"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

# Primeira versão
palavra_secreta = 'Perfume'

tentativa = 0

while True:
    palavra_formada = '*******'
    while palavra_formada != palavra_secreta:
        letra = input('Digite uma letra: ')
        tentativa += 1

        if len(letra) > 1:
            print('Digite apenas uma letra')
            continue

        if letra == 'P' or letra == 'p':
            palavra_formada = 'P' + palavra_formada[1:]

        if letra == 'e':
            palavra_formada = palavra_formada[:1] + 'e' + palavra_formada[2:6] + 'e'
        
        if letra == 'r':
            palavra_formada = palavra_formada[:2] + 'r' + palavra_formada[3:]
        
        if letra == 'f':
            palavra_formada = palavra_formada[:3] + 'f' + palavra_formada[4:]
        
        if letra == 'u':
            palavra_formada = palavra_formada[:4] + 'u' + palavra_formada[5:]
        
        if letra == 'm':
            palavra_formada = palavra_formada[:5] + 'm' + palavra_formada[6:]
        
        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            print()
            print(f'A palavra era: {palavra_secreta}')
            print(f'Você conseguiu em {tentativa} tentativa(s)')
            print()

# Segunda versão
palavra_chave = 'perfume'
tentativas = 0
letras_acertadas = ''

while True:
    letra_tentativa = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_tentativa) > 1:
        print('Digite apenas uma letra.')
        break

    if letra_tentativa in palavra_chave:
        letras_acertadas += letra_tentativa
    
    palavra_formada = ''
    for ordem_letras in palavra_chave:
        if ordem_letras in letras_acertadas:
            palavra_formada += ordem_letras
        else:
            palavra_formada += '*'

    print(palavra_formada)
    
    if palavra_formada == palavra_chave:
        print()
        print('Parabéns! Você acertou a palavra chave!')
        print(f'A palavra chave era: {palavra_formada}')
        print(f'Você acertou em {tentativas} tentativas')
        letras_acertadas = ''
        tentativas = 0