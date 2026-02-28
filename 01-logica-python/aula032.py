"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um número inteiro: ')

if entrada.isdigit():
    numero = int(entrada)
    par_impar = numero % 2 == 0 # Se for True é PAR, Se for False é IMPAR.
    par_impar_texto = ''

    if par_impar:
        par_impar_texto = 'par'
    else:
        par_impar_texto = 'impar'
    
    print(f"O número {numero} é {par_impar_texto}")

else:
    print('Você não digitou um número inteiro.')





"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

"""

entrada = input('Digite a hora em números inteiros: ')

try:
    horario = int(entrada)

    if horario >= 0 and horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')
cont_nome = len(nome)

if cont_nome > 1:
    if cont_nome <= 4:
        print('O seu nome é curto')
    elif cont_nome >= 5 and cont_nome <= 6:
        print('O seu nome é normal')
    else:
        print('O seu nome é muito grande')
else:
    print('Digite mais de uma letra.')