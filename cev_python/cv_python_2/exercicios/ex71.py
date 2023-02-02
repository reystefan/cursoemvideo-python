valor = int(input('Digite o valor a ser sacado: R$'))
# sem50 = sem20 = sem10 = sem1 = 0
tot50 = tot20 = tot10 = tot1 = 0
novo_valor = valor

if novo_valor > 50:
    tot50 = novo_valor // 50
    novo_valor -= (tot50 * 50)

if novo_valor > 20:
    tot20 = novo_valor // 20
    novo_valor -= (tot20 * 20)

if novo_valor > 10:
    tot10 = novo_valor // 10
    novo_valor -= (tot10 * 10)

if novo_valor > 1:
    tot1 = novo_valor // 1
    novo_valor -= (tot1 * 10)

print(f'Total de {tot50} cédulas de R$50.')
print(f'Total de {tot20} cédulas de R$20.')
print(f'Total de {tot10} cédulas de R$10.')
print(f'Total de {tot1} cédulas de R$1.')
