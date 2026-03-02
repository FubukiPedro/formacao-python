operador = ''
while operador != 'sair':
    operador = input('Qual operador deseja utilizar? (+ - * / // % **) ')

    if len(operador) > 1 and (operador not in ('//', '**', 'sair')):
        print('Digite apenas um operador. (Com excessão de "//, ** e sair")')

    elif operador not in ('+', '-', '*', '/', '//', '%', '**', 'sair'):
        print('Você não digitou um operador válido.')

    else:
        if operador == 'sair':
            print('Você digitou sair')
            break
        else:
            try:
                calculo1 = float(input('Digite o primeiro valor: '))
                calculo2 = float(input('Digite o segundo valor: '))

                resultado_calculo = 0
                if operador == '+':
                    calculo = 'soma'
                    resultado_calculo = calculo1 + calculo2
                elif operador == '-':
                    calculo = 'subtração'
                    resultado_calculo = calculo1 - calculo2
                elif operador == '*':
                    calculo = 'multiplicação'
                    resultado_calculo = calculo1 * calculo2
                elif operador == '/':
                    calculo = 'divisão'
                    resultado_calculo = calculo1 / calculo2
                elif operador == '//':
                    calculo = 'divisão inteira'
                    resultado_calculo = calculo1 // calculo2
                elif operador == '%':
                    calculo = 'resto da divisão'
                    resultado_calculo = calculo1 % calculo2
                elif operador == '**':
                    calculo = 'potência'
                    resultado_calculo = calculo1 ** calculo2

                if '.0' in str(resultado_calculo):
                    print(f'A {calculo} de {int(calculo1)} {operador} {int(calculo2)} é igual a: {int(resultado_calculo)}')
                else:
                    print(f'A {calculo} de {calculo1} {operador} {calculo2} é igual a: {resultado_calculo}')
            except:
                print('Você não digitou um número válido')
    print()