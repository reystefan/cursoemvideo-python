listagem = []
for c in range(0, 5):
    numero = int(input('Valor: '))
    if c == 0 or numero > listagem [-1]:
        listagem.append(numero)
        print('Adicionado ao final da lista...')
    else:
        for pos in range(0, len(listagem)):
            if numero <= listagem[pos]:
                listagem.insert(pos, numero)
                print(f'Valor {numero} adicionado na posição {pos}.')
                break


        


print(listagem)