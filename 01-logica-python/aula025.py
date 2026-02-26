"""
Interpolação básica de strings
s       -   string
d e i   -   int
f       -   float
x e X   -   Hexadecimal (ABCDEF0123456789)

'Texto %s' % variavel
"""

nome = 'Pedro'
idade = 20
salario = 2000.00000
print('O %s tem %d anos de idade e recebe R$%.2f reais' % (nome, idade, salario))
print('O hexadecimal de %d é %04X' % (salario, 2000))