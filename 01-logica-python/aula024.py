# Operadores in e not in
# Strings são iteráveis

# in = entre (está entre) / not in = não entre (não está entre)

#  0 1 2 3 4 5
#  P e d r o
# -6-5-4-3-2-1

nome = 'Pedro'
print(nome[2])
print(nome[-2])

print()

print('dro' in nome)
print('Hen' in nome)

print()

print('dro' not in nome)
print('Hen' not in nome)

print()

seunome = input('Digite o seu nome: ')
encontrar = input('O que deseja contratar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')