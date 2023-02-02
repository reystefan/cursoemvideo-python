pessoas = []
pessoa = {}
sexo = ''
resp = ''
soma_idade = 0
media_idade = 0
mulheres = []
idade_acima_media = []

while True:
    pessoa['nome'] = input('Nome: ').strip().title()

    while True:
        sexo = input('Sexo (M ou F): ').strip().upper()[0]
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('ERRO. Digite apenas M ou F.')
    
    pessoa['sexo'] = sexo
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())


    while True:
        resp = (input('Quer continuar? S/N ')).strip().upper()[0]
        if resp == 'S' or resp =='N':
            break
        else:
            print('ERRO, Digite apenas S ou N.')
    
    if resp == 'N':
        break

print(f'A) Um total de {len(pessoas)} cadastradas.')
media_idade = soma_idade / len(pessoas)
print(f'B) A média de idade é {media_idade}')

for i in pessoas:
    if i['sexo'] == 'F':
        mulheres.append(i.copy())
    if i['idade'] > media_idade:
        idade_acima_media.append(i.copy())

print('C) Mulheres cadastradas: ')
for m in mulheres:
    print(f'    {m["nome"]};')

print('D) Lista de pessoas que estão acima da média:')
for p in idade_acima_media:
    print('     ', end='')
    for k, v in p.items():
        print(f'{k} = {v};', end=' ')
    print()

print('<< ENCERRADO >>')
            

