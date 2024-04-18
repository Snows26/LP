# O que o programa faz?
#   - Filtra os números negativos dos positivos
#   - Transforma para o tipo float
#   - Tira a média dos números positivos
#   - E imprimi no final, todos os numeros positivos digitados e a média

from functools import reduce

entrada = lambda : [float(input()) for _ in range(0,6)]
positivo = lambda l: list(filter(lambda x: x > 0, l))
qntd = lambda l: len(positivo(l))
soma = lambda l: reduce(lambda x, y: x + y, positivo(l))
media = lambda l : soma(l) / qntd(l)
saida = lambda l : str(positivo(l))+ " \n Média dos positivos: %.1f" %media(l)


print("Insira 6 números aleatórios: ")
print(saida(entrada()))



