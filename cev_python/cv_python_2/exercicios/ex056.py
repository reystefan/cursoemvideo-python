soma_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
tot_mulheres_menos_20_anos = 0
media = 0
qtd_homem = 0

for pessoa in range (1, 5):
    print(f'{"-"*6} {pessoa} ª pessoa {"-"*6}')
    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo (M ou F): ').strip().upper()
    print('\n', end='')

    soma_idade += idade

    if qtd_homem == 0 and sexo == 'M':
        qtd_homem += 1
        idade_mais_velho = idade
        nome_mais_velho = nome
    elif sexo == 'M' and idade > idade_mais_velho:
        nome_mais_velho = nome
        idade_mais_velho = idade
    elif sexo == 'F' and idade < 20:
        tot_mulheres_menos_20_anos += 1

media = soma_idade / pessoa

print(f'Média de idade do grupo: {media}')
print(f'Homem mais velho: {nome_mais_velho}')
print(f'Mulheres com menos de 20 anos: {tot_mulheres_menos_20_anos}')
        
