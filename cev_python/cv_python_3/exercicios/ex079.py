numeros = []

while True:
    numero = int(input('Digite um valor: '))
    if numero in numeros:
        print(f'O número {numero} já existe na lista, portanto não foi adicionado.')
    else:
        numeros.append(numero)

    sair = input('Quer continuar? [S/N] ').strip().upper()[0]
    if sair == 'N':
        break

print(numeros)
numeros.sort()
print(numeros)