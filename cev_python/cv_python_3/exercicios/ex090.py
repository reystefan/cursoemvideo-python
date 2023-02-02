alunos = {}

alunos['nome'] = input('Nome: ')
alunos['media'] = float(input('Média: '))

if alunos['media'] < 6:
    alunos['situacao'] = 'reprovado'
else:
    alunos['situacao'] = 'aprovado'

for k, v in alunos.items():
    print(f'{k} é {v}')

