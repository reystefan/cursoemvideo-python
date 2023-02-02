def dobra(lst):  # Em alguns momentos, ao invés de utilizar o desempacotamento, é melhor a utilização de listas
    pos = 0      #  pois nas listas podemos alterar os valores contidos nela, que no caso, serão nossos parâmetros
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)
