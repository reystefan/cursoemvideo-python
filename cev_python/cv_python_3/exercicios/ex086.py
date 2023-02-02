matrix = [[], [], []]

for linha in range(0, 3):
    print(f'\nLinha {linha}')
    for coluna in range(0, 3):
        matrix[linha].append(int(input(f'Digite o {coluna+1}º valor: ')))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matrix[linha][coluna]:^5}]', end='')
    print()
