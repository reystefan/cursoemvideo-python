numero = int(input('Digite um número inteiro: '))

for c in range(1, 11):
    print(f'{numero} x {c:>2} = {numero * c:>2}')