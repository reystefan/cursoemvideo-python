from datetime import date

ano_nascimento = int(input('Digire o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f'Você completou {idade} anos, está na hora de se alistar!')
elif idade > 18:
    passou_prazo = idade - 18
    print(f'Seu prazo para o alistamento já passou em {passou_prazo} anos.')
else:
    falta_prazo = 18 - idade
    print(f'Faltam {falta_prazo} anos para você se alistar.')
