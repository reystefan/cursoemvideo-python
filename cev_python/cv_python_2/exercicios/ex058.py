from random import randint

numero_computador = randint(0, 10)
print('Computador: Acabei de pensar em um número... Será que você consegue adivinhar?')
numero_jogador = int(input('Digite um número: '))
tentativas = 0

while numero_jogador != numero_computador:
    numero_jogador = int(input('Você errou! Tente outro número: '))
    tentativas += 1

print(f'{numero_jogador = } {numero_computador = }')
print('Você GANHOU!')
print(f'Com {tentativas} tentativas.')