dados_jogador = {}

dados_jogador['nome'] = input('Nome do jogador: ')

qtd_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))

gols = []
totgols = 0
for pt in range(0, qtd_partidas):
    gols.append(int(input(f'Quantos gols na partida {pt+1}? ')))
    totgols += gols[pt]

dados_jogador['gols'] = gols[:]
dados_jogador['total'] = totgols

print(dados_jogador, end='\n\n')

for k, v in dados_jogador.items():
    print(f'O campo {k} tem o valor {v}')
print()

print(f'O jogador {dados_jogador["nome"]} jogou {qtd_partidas} partidas.')
for pos, val in enumerate(dados_jogador['gols']):
    print(f'    => Na partida {pos+1}, fez {val} gols.')
print(f'Foi um total de {dados_jogador["total"]} gols.')

totgols2 = sum(gols)
print(totgols2)  #  Outra forma de somar valores de uma Lista