expressao = input('Expressão: ')
qtd_parent = 0

for char in expressao:
    if char == '(':
        qtd_parent += 1
    elif char == ')':
        qtd_parent -= 1
    if qtd_parent < 0:
        break

if qtd_parent == 0:
    print(f'A expressão {expressao} é válida.')
else:
    print(f'A expressão {expressao} é inválida.')
