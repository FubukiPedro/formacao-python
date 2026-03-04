""" while/else """

string = 'Valorqualquer'

i = 0
while i < len(string):
    letra = string[i]
    print(letra)

    if letra == ' ':
        print('Encontrei um espaço na string')
        break

    i += 1
    
else:
    print('Não encontrei um espaço na string.')

print('Fora do while.')