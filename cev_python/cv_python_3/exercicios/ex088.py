from random import randint

qtd_jogos = int(input('Quantos jogos quer? '))
jogadas = []

for jogo in range(0, qtd_jogos):
    numeros = []
    cont = 0

    while True:
        num = randint(1, 60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont >= 6:
            break

    jogadas.append(numeros[:])
    print(f'Jogo {jogo+1}: {numeros}')
    numeros.clear()