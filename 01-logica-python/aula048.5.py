"""
imutáveis (int, float, str, bool, tuple):
    = cria um novo valor independente

mutáveis (list, dict, set):
    = cria outra referência para o mesmo objeto na memória
    .copy() cria uma cópia independente
"""

lista_a = ['Carro', 'Maria', 1, True, 1.2]
lista_b = lista_a # Mesmo se eu alterar algo na lista_a depois desse código, vai alterar aqui também
lista_c = lista_a.copy() # Mas com o copy não, porque ele cria uma nova

lista_a[0] = 'Pedro'

print(lista_a)
print(lista_b)
print(lista_c)