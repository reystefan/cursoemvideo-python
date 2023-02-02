dados_jogador = {}
jogadores = []

while True:
    dados_jogador['nome'] = input('Nome do jogador: ').strip().title()
    qtd_partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou? '))
    gols = []
    totgols = 0
    for pt in range(0, qtd_partidas):
        gols.append(int(input(f'    Quantos gols na partida {pt+1}? ')))
        totgols += gols[pt]

    dados_jogador['gols'] = gols[:]
    dados_jogador['total'] = totgols
    jogadores.append(dados_jogador.copy())
    dados_jogador.clear()

    while True:
        resp = input('Quer continuar? S/N ').strip().upper()[0]
        if resp == 'S' or resp =='N':
            break
        print('ERRO. Digite apenas S ou N.')
    
    if resp == 'N':
        break
    else:
        continue

print('-='*50)
print(f'{"cod":<4}{"nome":<12}{"gols":<15}{"total"}')
print('-'*38)

for pos, j in enumerate(jogadores):
    print(f'{pos:>3} {str(j["nome"]):<12}{str(j["gols"]):<15}{str(j["total"])}')
print('-'*38)

while True:
    opcao = int(input('Mostrar dados de quL jogador? (999 para parar.) '))
    if opcao == 999:
        break
    elif opcao < 0 or opcao >= len(jogadores):
        print('ERRO. Digite uma opção que esteja na lista.')
        continue
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}:')
        for pos, v in enumerate(jogadores[opcao]["gols"]):
            print(f'    No jogo {pos+1} fez {v} gols.')
        print('-'*38)




# totgols2 = sum(gols)
# print(totgols2)  #  Outra forma de somar valores de uma Lista