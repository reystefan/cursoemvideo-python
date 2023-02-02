lista = list()
while True:
    lista.append(int(input('Número: ')))
    
    resposta = input('Quer continuar? S/N ').strip().upper()[0]
    print()
    if resposta == 'N':
        break

lista.sort(reverse=True)

if 5 in lista:
    print(f'O número 5 está na lista na posição {lista.index(5)}')
else:
    print('O número 5 não está na lista.')


print(f'{len(lista)} números foram digitados.')
print(lista)