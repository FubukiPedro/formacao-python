# Operadores lógicos
# and (e) or (ou) not (não)

# and - Todas as condições precisam ser verdadeiras.
# se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
# são considerados falsy (que vc já viu) 0 0.0 '' False
# também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntra ou [S]aida: ')
senha_digitada = input('Digite uma senha: ')

senha_permitida = '1234'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print()

print(True and False and True) # false
print(True and 0 and True) # 0 = false, então é 0
print(False and 5 and True) # retornou o primeiro false, se o primeiro valor for false, o and já para ali.

print()

# O and só retorna False se o numero for 0 0.0 '' False
print(True and 5 and True)
print(5 and 5 and True)
print(5 and 5 and 5)
print(True and True and 5)
# se todos forem True, ele retorna o ultimo valor