"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

# Jeito 1
lista = ['Maria', 'Pedro', 'Pandinha', 'Piranha']
lista.append('Henrique')
indice = 0
for nomes in lista:
    print(f'{indice} {nomes}')
    indice += 1

print()

# Jeito 2
lista = ['Maria', 'Pedro', 'Pandinha', 'Piranha']
lista.append('Henrique')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))