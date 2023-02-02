pessoas = []
dados = []
maior_peso = 0
menor_peso = 0
nome_mais_pesado = []
nome_mais_leve = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    if maior_peso == 0 == menor_peso:
        menor_peso = maior_peso = dados[1]

    elif dados[1] > maior_peso:
        maior_peso = dados[1]
        
    elif dados[1] < menor_peso:
        menor_peso = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    resp = input('Quer continuar? S/N ').upper().strip()[0]
    if resp == 'N':
        break

for p in pessoas:
    if p[1] == maior_peso:
        nome_mais_pesado.append(p[0])
    elif p[1] == menor_peso:
        nome_mais_leve.append(p[0])

print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'Os mais pesados foram {nome_mais_pesado} com {maior_peso} Kg.')
print(f'Os mais leves foram {nome_mais_leve} com {menor_peso} Kg.')

