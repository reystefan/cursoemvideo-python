from random import randint

num_computador = randint(0, 10)
num_jogador = None
print('Sou seu computador e pensei em um número, tente adivinhar...')
tentativas = 0

while num_jogador != num_computador:
    if tentativas != 0:  #  Se não for a primeira tentativa
        print('Você errou! Tente novamente.')
    num_jogador = int(input('Digite um numero: '))
    tentativas += 1

print(f'Numero computador {num_computador} e jogador {num_jogador}. Você conseguiu!')
print(f'{tentativas = }')