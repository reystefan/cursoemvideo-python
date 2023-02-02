numero = produto = 0

print('Tabuada do número que você digitar.')

while True:
    numero = int(input('Digite um número: '))
    print(f'{"-"*20}')
    if numero < 0:
        break
    else:
        for c in range(1, 11):
            produto = numero * c
            print(f'{numero:^2} * {c:^2} = {produto:^2}')
    print(f'{"-"*20}')
    
