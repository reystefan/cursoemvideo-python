valores = (int(input('Digite um valor: ')), 
            int(input('Outro: ')), 
            int(input('Outro: ')), 
            int(input('Outro: ')))

print(valores.count(9))

print(valores.index(3) if 3 in valores else 'O valor 3 não está na tupla.')

print('Valores pares: ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ')
