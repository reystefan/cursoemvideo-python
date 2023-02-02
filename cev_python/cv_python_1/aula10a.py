nome = input('Qual é seu nome: ')

if nome == 'Gustavo':
    print('Que nome lindo você tem!')

print(f'Bom dia, {nome}!')

#=====================================================================

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

print(f'A sua média foi {media:.1f}')
print(f'Parabéns!' if media >= 6 else f'Estude mais!') # Condições simplificadas
