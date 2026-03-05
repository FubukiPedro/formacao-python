# o que aprendemos com while também funciona no for (continue, break, else, etc)o que aprendemos com while também funciona no for (continue, break, else, etc)

for i in range(10):

    if i == 2:
        print('o "i" chegou no 2, pulando...')
        continue # Esse continue faz com que volte ao inicio, então o if i == 2 deu positivo e o continue pula o restante da iteração atual e vai para a próxima 
                 # iteração do loop, e como tem um for que seguira dando next... O continue faz o loop pular o restante da iteração atual e o for pega o próximo valor do iterador (next()), que no caso será 3., 
                 # por isso não imprimiu o for j in range(1, 3), porque o código não seguiu sendo executado, ele retornou ao for

    if i == 8:
        print('o "i" chegou no 8') #como usei o "break", então ele vai sair do for antes de completar o 10 e o for else não vai executar')
        break # caso chegue ao break, o break interrompe a execução do for, então ele para de executar e sair desse for e como o for j in range(1, 3) 
              # está dentro do for que houve o break, então ele não vai mais ser executado.

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso')
    # e o else não será executado, mas caso o for consiga percorrer por completo, ele pararia no StopIteration e ai o else seria ativado
    # então basicamente o else do for executa somente se o loop terminar normalmente.