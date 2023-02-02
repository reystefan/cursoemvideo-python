from random import randint
from time import sleep

print(f'{"JOKENPÔ":=^20}')

jogou = ('PEDRA', 'PAPEL', 'TESOURA')
jogada_computador = randint(1, 3)
jogada_humano = int(input('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Escolha uma jogada: '''))

if 1 <= jogada_humano <=3:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print(f'{"-="*20}')
    print(f' Computador jogou {jogou[jogada_computador-1]} \n Jogador jogou {jogou[jogada_humano-1]}')
    print(f'{"-="*20}')
    
    if jogada_computador != jogada_humano:  # Se não houver empate

        if jogada_computador == 1:  #  Computador jogou PEDRA
            if jogada_humano == 2:  #  Jogador jogou PAPEL
                print('JOGADOR VENCEU')
            elif jogada_humano == 3: #  Jogador jogou TESOURA
                print('COMPUTADOR VENCEU')
        elif jogada_computador == 2:  #  Computador jogou PAPEL
            if jogada_humano == 1:  #  Jogador jogou PEDRA
                print('COMPUTADOR VENCEU')
            elif jogada_humano == 3:  #  Jogador jogou TESOURA
                print('JOGADOR VENCEU')
        elif jogada_computador == 3:   #  Computador jogou TESOURA
            if jogada_humano == 1:  #  Jogador jogou PEDRA
                print('JOGADOR VENCEU')
            elif jogada_humano == 2:  #  Jogador jogou PAPEL
                print('COMPUTADOR VENCEU')
    else:
        print('EMPATE')
        
else:
    print('Digite uma jogada válida.')