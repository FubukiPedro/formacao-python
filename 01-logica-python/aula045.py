"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

Quando você usar o for, a primeira coisa que o for faz é solicitar pelo iterador do elemento
"""
# for letra in texto
texto = 'Pedro'  # iterável
iterador = iter(texto) # Poderia ser range, mas vou utilizar str

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

print()

for letra2 in texto:
    print(letra2)

"""
texto = iter('Pedro')  #__iter__() # iterator
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(next(texto))
print(next(texto))
print(next(texto)) # A partir daqui vai dar um erro.
"""

# o for em python funciona basicamente como um loop chamando next() várias vezes no iterador até acabar.