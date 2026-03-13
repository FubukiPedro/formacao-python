"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Pedro', 'Maria', 'Pandinha']
lista.append('Piranha')

for item in enumerate(lista):
    print(item)

print()

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

print()

for indice, nome in enumerate(lista):
    print(indice)
    print(nome)