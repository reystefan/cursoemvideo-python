from datetime import date

ano_atual = date.today().year
tot_maioridade = 0
tot_menoridade = 0


for pessoa in range (1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = ano_atual - ano_nascimento

    if idade < 21:
        tot_menoridade += 1
    elif idade >= 21:
        tot_maioridade += 1

print(f'Um total de {tot_menoridade} pessoas ainda não atingiu a maioridade '
f'e um total de {tot_maioridade} pessoas já atingiu a maioridade.')