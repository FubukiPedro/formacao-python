"""
split e join com list e str

split = ele separa uma string com base no que você informar, se deixar .split(',') ele vai separar a cada "," (split - divide uma string (list))
strip = strip() remove: espaços do começo e espaços do final
join = join() une strings de uma lista usando um separador. (une uma string)

"""

frase = '  Olha só que  ,  coisa interessante  '

lista_palavras = frase.split(' ')
lista_frases_crua = frase.split(', ')

lista_frases = []

'''for i, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[i].strip())
    print(lista_frases[i])'''

# ou 

for frase in lista_frases_crua:
    frase_limpa = frase.strip()
    lista_frases.append(frase_limpa.strip())
    print(frase_limpa)
    print(lista_frases)

print()

print(lista_palavras)
print(lista_frases_crua)
print(lista_frases)

print()

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)