primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if int(primeiro_valor) > int(segundo_valor):
    print(f'{primeiro_valor} é maior que o {segundo_valor}')
elif int(segundo_valor) > int(primeiro_valor):
    print(f'{segundo_valor=} é maior que o {primeiro_valor=}')
else:
    print(f'O valor de primeiro_valor e segundo_valor são igual (valor = {primeiro_valor})')