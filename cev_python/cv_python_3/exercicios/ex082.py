lista = list()
while True:
    lista.append(int(input('Valor: ')))

    resposta = input('Quer continuar? S ou N ').strip().upper()[0]
    if resposta == 'N':
        break

pares = []
impares = []

for valor in lista:
    if valor % 2 == 0:
        pares += [valor]  #  Da no mesmo do de baixo
    else:
        impares.append(valor)

print(f'Lista inicial: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
