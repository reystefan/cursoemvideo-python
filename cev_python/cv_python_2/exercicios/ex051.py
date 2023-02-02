print(f'{"="*40}')
print(f'{"10 TERMOS DE UMA P.A.":^40}')
print(f'{"="*40}')

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for c in range(1, 11):
    print(termo, end=' → ' if c < 10 else '')
    termo += razao