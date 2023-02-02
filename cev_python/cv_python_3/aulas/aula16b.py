a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   #  Junta as tuplas

print(c)

c = b + a   # Ordem faz diferença nas junções entre tuplas

print(c)

print(c.count(5)) #  Quantas vzs aparece o elemento 5 dentro da tupla c

print(c.index(8)) # Qual o índice onde está o elemento 8 (primeira ocorrencia da esq para a dir)

print(c.index(5, 1)) # Mesma coisa porém começando da posição 1