"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y =', x + y + z)

soma(1, 2, 3)
soma(2, 4, 5)
soma(z=1, y=2, x=1)
soma(z=1, x=2, y=1)
soma(1, y=2, z=1)

print(1, 2, 3, sep='-')