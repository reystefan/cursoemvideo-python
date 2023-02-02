for contagem in range(1, 51):
    if contagem % 2 == 0:
        print(contagem, end = ' ')

print('\n\n Outra forma, sem o if e economizando na qtd de laços\n')

for contagem in range(2, 51, 2):
    print(contagem, end = ' ')