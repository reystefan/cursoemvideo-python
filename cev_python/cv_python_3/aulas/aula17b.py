"""
- list.append(x): Adiciona um item ao fim da lista.
- 
list.insert(i, x): Insere um item em uma dada posição i.
- 
del(): Deleta um elemento da lista ou a própria lista.

- list.pop(i): Remove o item de posição i da lista e o retorna. Caso i não seja especificado, retorna o último elemento da lista.
- 
list.remove(x): Remove o primeiro elemento, cujo valor seja x.

- list.clear(): Remove todos os elementos da lista.

- list.index(x[, start[, end]]): Retorna o índice do primeiro elemento cujo valor seja x.

- list.count(x): Retorna o número de vezes que o valor x aparece na lista.

- list.sort(key=None, reverse=False): Ordena os items da lista (os argumentos podem ser usados para customizar a ordenação).
- 
list.reverse(): Reverte os elementos da lista.
- list.copy(): Retorna uma lista com a cópia dos elementos da lista de origem.
"""

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)
num.remove(2)  #  Remove a primeira ocorrencia do parametro indicado

if 4 in num:
    num.remove(4)

print(num)
print(f'Essa lista tem {len(num)} elementos.')