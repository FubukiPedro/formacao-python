"""
Iterando strings com while
"""
#       012345678910
nome = 'Pedro Henrique'  # Iteráveis
#      1110987654321

tamanho_nome = len(nome)
print(nome)
print(tamanho_nome, 'letras')

# Forma 1
cont_nome = 0
while cont_nome < tamanho_nome: 
    print(f'*{nome[cont_nome]}', end='')
    cont_nome += 1

print('*')

# Forma 2
cont_nome = 0
novo_nome = ''
while cont_nome < tamanho_nome:
    letra = nome[cont_nome]
    novo_nome += f'*{letra}'
    cont_nome += 1

novo_nome += '*'
print(novo_nome)