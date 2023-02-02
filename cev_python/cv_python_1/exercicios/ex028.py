from random import randint
from time import sleep

numero = randint(0, 5)
numero_usuario = int(input('Digite um número de 0 a 5: '))
print('Pensando em um numero. . .')
sleep(3)

if numero_usuario == numero:
    print(f'Você venceu! O número escolhido foi {numero} que é igual ao que'
    f'você digitou: {numero_usuario}')
else:
    print(f'O número digitado foi {numero_usuario} e o número escolhido'
    f' foi {numero}. Você perdeu!')
