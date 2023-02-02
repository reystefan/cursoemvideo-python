listagem = []

for item in range(0, 5):
    numero = int(input('Valor: '))
    if item == 0 or numero > listagem[-1]:
        listagem.append(numero)
        print(f'Valor {numero} adicionado na última posição.')
    else:
        for pos, valor in enumerate(listagem):
            if numero <= valor:
                listagem.insert(pos, numero)
                print(f'Valor {numero} adicionado na posição {pos}.')
                break

print(listagem)


