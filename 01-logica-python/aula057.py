salas = [
    ['Maria', 'Helena'],
    ['Eliane'],
    ['Luiz', 'João', 'Eduarda', (10, 20, 30, 40)]
]

print(salas)
print(salas[1][0])
print(salas[0][1])
print(salas[2][2])
print(salas[2][3][2])

print()

for sala in salas:
    print(f'A sala é {sala}')
    for alunos in sala:
        print(alunos)
    print()