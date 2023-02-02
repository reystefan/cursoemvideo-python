from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('A categoria do atleta é MIRIM')
elif idade <= 14:
    print('A categoria do atleta é INFANTIL')
elif idade <= 19:
    print('A categoria do atleta é JUNIOR')
elif idade <= 25:
    print('A categoria do atleta é SÊNIOR')
elif idade > 25:    #  Ou else:
    print('A categoria do atleta é MASTER')
 