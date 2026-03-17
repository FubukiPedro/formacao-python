# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Julia']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, s, *_, ap, pn, u = lista
print(p, s, ap, pn, u) # Primeiro, segundo, antepenúltimo, penúltimo e último

print()

print('Maria', 'Helena', 1, 2, 3, 'Julia')
print(*lista)
print(*string, sep='*')
print(*tupla)

print()

print(salas)
print(*salas)
print(*salas, sep='\n')