"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args):
    total = 0
    for numero in args:
        total += numero
        #print(f'Número: {numero} - Total: {total}')
    return total

soma_1_2_3 = soma(1, 2, 3)
print(f'soma 1, 2 e 3 = {soma_1_2_3}')

soma_4_5_6 = soma(4, 5, 6)
print(f'soma 4, 5 e 6 = {soma_4_5_6}')

numeros = 7, 8, 9, 10, 11, 12, 13
outra_soma = soma(*numeros)
#outra_soma = soma(7, 8, 9, 10, 11, 12, 13)
print(outra_soma)

print(sum((7, 8, 9, 10, 11, 12, 13)))
print(sum(numeros))