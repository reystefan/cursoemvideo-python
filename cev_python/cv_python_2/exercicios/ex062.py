print(f'{"="*40}')
print(f'{"10 TERMOS DE UMA P.A.":^40}')
print(f'{"="*40}')

termo = int(input('Digite o 1º termo: '))
razao = int(input('Digite a razão: '))
contador = 0
qtd_termos = 10

while contador < qtd_termos:
    print(termo, end=' → ')
    termo += razao
    contador += 1
    if contador == qtd_termos:
        print('PAUSA')
        mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
        if mais_termos != 0:
            qtd_termos += mais_termos
        else:
            print(f'Fim da execução com {qtd_termos} termos.')
        
