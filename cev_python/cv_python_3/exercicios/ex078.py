lista = []
for c in range(5):
    lista.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = lista[0]
        menor = lista[0]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]

print(f'O maior valor foi {maior} na posição:', end=' ')

for pos, valor in enumerate(lista):
    if valor == maior:
        print(pos, end=' ')

print(f'\nO menor valor foi {menor} na posição:', end=' ')

for pos, valor in enumerate(lista):
    if valor == menor:
        print(pos, end=' ')



