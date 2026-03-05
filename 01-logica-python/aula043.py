# Introdução ao for / in - estrutura de repetição para coisas finitas

texto = 'Python'

novo_texto = ''
for i in texto:
    novo_texto += f'*{i}'
    print(i)
print(novo_texto + '*')