def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')

jogador = input('Nome: ').strip()
gols = input('Gols: ')

if gols.isnumeric():
    gols = int(gols)
    if jogador:
        ficha(jogador, gols)
    else:
        ficha(gols=gols)
else:
    if jogador:
        ficha(jogador)
    else:
        ficha()