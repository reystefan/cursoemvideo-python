print('Calculador de fatorial!')

numero = int(input('Digite um número inteiro: '))
fatorial = 1

while numero > 1:
    fatorial *= numero
    print(f'{numero}', end='')
    numero -= 1
    print(f'{numero} = {fatorial}' if numero == 1 else ' → ', end='')

print('\nFim')