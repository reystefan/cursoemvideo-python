alunos = []

while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2)/ 2
    alunos.append([nome, [nota_1, nota_2], media])

    resp = input('Quer continuar? S/N ').upper().strip()[0]
    if resp == 'N':
        break

print('-'*40)
print(f'{"No.":<4}{"NOME":<12}{"MÉDIA":>8}')

for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<12}{a[2]:>8.1f}')

print('-'*40)

while True:
    num_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if num_aluno == 999:
        print('\nFINALIZANDO. . .')
        break
    else:
        if num_aluno < 0 or num_aluno > len(alunos) - 1:
            print('Número de aluno inválido. ', end='')
        else:
            print(f'As notas do aluno(a) {alunos[num_aluno][0]} foram {alunos[num_aluno][1]}\n')

