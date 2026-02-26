# Operadores lógicos
# and (e) or (ou) not (não)

# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira. 
# se qualquer valor for considerado verdadeiro, a expressão inteira será avaliada naquele valor.

# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntra ou [S]aida: ')
senha_digitada = input('Digite uma senha: ')

senha_permitida = '1234'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print()

senha = input('Digite a senha: ') or 'Sem senha'
print(senha)