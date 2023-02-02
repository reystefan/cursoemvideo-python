from random import randint


numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(numeros)

menor = numeros[0]
maior = numeros[0]

for n in numeros:
    if n < menor:
        menor = n
    elif n > maior:
        maior = n

print(f'Menor número: {menor}')
print(f'Maior número: {maior}')

print('Utilizando métodos:')
print(f'Menor número: {min(numeros)}')
print(f'Maior número: {max(numeros)}')
