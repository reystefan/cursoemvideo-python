maioridade = qtd_homem = mulher_idade_menor_q_20 = 0

while True:
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ''

    while 'F' != sexo != 'M': 
        sexo = input('Sexo [M ou F]: ').strip().upper()[0]
        if sexo not in 'MmFf':
            print('Informação inválida, tente novamente.')

    if idade > 18:
        maioridade += 1

    if sexo == 'M':
        qtd_homem += 1

    if sexo in 'Ff' and idade < 20:
        mulher_idade_menor_q_20 += 1

    while True:
        resposta = input('Quer continuar? (S ou N): ').strip().upper()[0]
        if resposta not in 'SsNn':
            print('Resposta inválida, tente novamente.')
        else:
            break

    if resposta in 'Nn':
        print('Finalizando. . .\n')
        break

print(f'Maiores de 18 anos: {maioridade}')
print(f'Homens: {qtd_homem}')
print(f'Mulheres com menos de 20 anos: {mulher_idade_menor_q_20}')