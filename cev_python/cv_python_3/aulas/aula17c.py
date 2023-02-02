valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'\nNa posição {c} encontrei o valor {v}!')

val = []
for cont in range(0, 5):
    val.append(int(input('Digite um valor: ')))

print(val)


#    OBS

a = [2, 3, 4, 7]
b = a   # Cria uma ligação entre as listas, fazendo com que qlqr alteraçao feita em uma, também altera a outra.
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:]   # Usando Fatiamento, b recebe todos os valores de a, sem que haja uma ligação entre as listas, sendo apenas uma cópia
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
