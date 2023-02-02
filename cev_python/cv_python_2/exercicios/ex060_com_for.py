numero = int(input('Digite um número: '))
fatorial = 1

print(f'O fatorial de {numero}! = ', end='')
for contador in range(numero, 0, -1):
    fatorial *= contador
    print(f'{contador} x ' if contador != 1 else f'{contador} = {fatorial}', end='')
