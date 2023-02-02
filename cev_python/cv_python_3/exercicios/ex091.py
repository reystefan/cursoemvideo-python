from random import randint
from operator import itemgetter

jogador = {}

for j in range(1, 5):
    jogador[f'jogador{j}'] = randint(1, 6)

for k, v in jogador.items():
    print(f'O {k} tirou {v} no dado.')
print()

ranking = []
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)

print('As posições foram: \n')
for pos, j in enumerate(ranking):
    print(f'{pos+1}º lugar: {j[0]} com {j[1]}')
