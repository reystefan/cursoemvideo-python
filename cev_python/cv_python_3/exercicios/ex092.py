from datetime import date

dados = {}
dados['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = (date.today().year) - ano_nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratacao'] + 35) - ano_nascimento

for k, v in dados.items():
    print(f'{k} tem o valor {v}')

