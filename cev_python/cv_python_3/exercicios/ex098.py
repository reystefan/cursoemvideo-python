from time import sleep

def contagem(i, f, p):
    print('-='*30)
    
    if p < 0:
        p *= (-1)

    print(f'Contagem de {i} até {f} de {p} em {p}')

    if f > i:
        for n in range(i, f+1, p):
            print(n, end=' ')
            sleep(0.2)
        print('FIM!')
    elif i > f:
        for n in range(i, f-1, -p):
            print(n, end=' ')
            sleep(0.2)
        print('FIM!')
    

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-='*30)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(i=inicio, f=fim, p=passo)