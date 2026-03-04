# Qual letra apareceu mais vezes na frase? (iterando strings com while)

frase = 'aaaoooo'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i + 1
        continue
    
    qtd_apareceu_mais_vezes_atual = frase.count(letra)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra
        
    i += 1

print(f'Letra que mais apareceu: {letra_apareceu_mais_vezes}')
print(f'Quantidade de vezes que apareceu: {qtd_apareceu_mais_vezes}')