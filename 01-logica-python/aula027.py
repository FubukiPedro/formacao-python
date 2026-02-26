"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321 (-9 -8 -7 -6 -5 -4 -3 -2 -1)
(Conta a partir do 0)

Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de caracteres da str (Conta a partir do 1)
"""

variavel = 'Olá mundo'
print(variavel[0:8]) # contou a partir do 0, mas ele para no 8 então no caso não contou o "o"
print(variavel[:9]) 
print(variavel[0:])
# ele coloca automático
print(variavel[::+2])
print(variavel[-1:-10:-1])
print(variavel[::-1])