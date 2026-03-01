"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Pedro Henrique'
outra_string = f'{string[:4]}ABC{string[5:]}'

print(string)
print(outra_string)

print(string.zfill(15))