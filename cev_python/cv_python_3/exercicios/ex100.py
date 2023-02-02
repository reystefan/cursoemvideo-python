from random import randint

def sorteia(lista):
    for v in range(0, 5):
        lista.append(randint(0, 9))
    
    print('Sorteando os 5 valores da lista: ', end='')
    for n in lista:
        print(n, end=' ')
    print('PRONTO!')

def somar(lst):
    soma = 0
    print(f'Somando os valores pares de {lst}, ', end='')
    for i in lst:
        if i % 2 == 0:
            soma += i
    print(f'temos {soma}')


numeros = []
sorteia(numeros)
somar(numeros)
