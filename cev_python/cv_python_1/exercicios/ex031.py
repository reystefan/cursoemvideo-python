distancia = float(input('Digite a distância da viagem (km): '))
preco = 0.50 * distancia if distancia <= 200 else 0.45 * distancia

print(f'O preco da viagem de {distancia}km será de R${preco:.2f}.')

#Ou
if distancia <= 200:
    preco_viagem = 0.50 * distancia
    print(f'O preco da viagem de {distancia}km será de R${preco_viagem:.2f}.')
else:
    preco_viagem = 0.45 * distancia
    print(f'O preco da viagem de {distancia}km será de R${preco_viagem:.2f}.')
