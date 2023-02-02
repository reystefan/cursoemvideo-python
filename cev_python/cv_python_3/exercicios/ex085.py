numeros = [[], []]

for n in range(0, 7):
    num = int(input(f'Digite o {n+1}º valor: '))

    if num % 2 == 0:
        numeros[0].append(num)
    elif num % 2 != 0:
        numeros[1].append(num)

numeros[0].sort()
numeros[1].sort()

print(f'Números pares: {numeros[0]}')
print(f'Números ímpares: {numeros[1]}')
