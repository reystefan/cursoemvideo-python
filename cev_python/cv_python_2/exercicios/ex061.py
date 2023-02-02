print(f'{"="*40}')
print(f'{"10 TERMOS DE UMA P.A.":^40}')
print(f'{"="*40}')

termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
contador = 0

while contador < 9:
    print(termo, end=' → ' if contador != 9 else '')
    termo += razao
    contador += 1
print(termo)
