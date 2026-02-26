"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# .isdigit() verifica se todos os caracteres da string são dígitos numéricos.
# .isdigit() funciona para qualquer string que tenha apenas números de 0 a 9, não importa se tem 1 dígito ou vários.

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
        numero_float = float(numero_str)
        print('Float:', numero_float)
        print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
        print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2}')
# else:
#     print('Isso não é um número')