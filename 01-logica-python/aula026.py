"""
> Formatação básica de strings
s - string
d - int
f - float
x ou X - Hexadecimal
.<número de dígitos>f / (Exemplo: 2000 com .2f ficaria 2000.00)

(Caractere)(><^)(quantidade) / (Exemplo: {variavel: >10})
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f"{variavel}")
print(f"{variavel: >7}")
print(f"{variavel: <7}.")
print(f"{variavel: ^7}.")

print(f'{1000.4873648123746:0=+10,.1f}')
# +001,000.5
# 0 serve para preencher com zero e o "=" faz o preenchimento acontecer ENTRE o sinal e o número [sinal][preenchimento][número]
# + → sempre mostrar sinal
# 10 → largura total 10 caracteres
# , → separador de milhar (O Python coloca vírgula a cada 3 dígitos da direita para a esquerda, e só atua na parte inteira)
# .1f → 1 casa decimal


print(f'O hexadecimal de 2000 é {2000:04X}')