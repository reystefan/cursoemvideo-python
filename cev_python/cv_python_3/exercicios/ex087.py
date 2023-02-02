matrix = [[], [], []]
pares = soma = maior = 0

for linha in range(0, 3):
    print(f'\nLinha {linha}')
    for coluna in range(0, 3):
        matrix[linha].append(int(input(f'Digite o {coluna+1}º valor: ')))

for linha in range(0, 3):
    soma += matrix[linha][2]

    for coluna in range(0, 3):
        if matrix[linha][coluna] % 2 == 0:
            pares += matrix[linha][coluna]

        if linha == 1:
            if coluna == 0 or matrix[1][coluna] > maior:
                maior = matrix[1][coluna]

        print(f'[{matrix[linha][coluna]:^5}]', end='')
    print()

# maior = 0

# for valor in matrix[1]:       # Percorre cada valor da segunda linha da matriz
#     if valor == 0 or valor > maior:
#         maior = valor

print(f'A soma de todos os pares é {pares}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior valor da segunda linha é {maior}')
