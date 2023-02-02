peso_maior_atual = 0
peso_menor_atual = 0


# for pessoa in range (1, 6):
#     peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
#     if peso > peso_maior_atual:
#         peso_maior_atual = peso
#     elif peso < peso_maior_atual:
#         if peso_menor_atual == 0:
#             peso_menor_atual = peso
#         elif peso < peso_menor_atual:
#             peso_menor_atual = peso

# print(f'Maior peso: {peso_maior_atual}')
# print(f'Menor peso: {peso_menor_atual}')

for pessoa in range (1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        peso_maior_atual = peso
        peso_menor_atual = peso
    elif peso > peso_maior_atual:
        peso_maior_atual = peso
    elif peso < peso_menor_atual:
        peso_menor_atual = peso

print(f'Maior peso: {peso_maior_atual}')
print(f'Menor peso: {peso_menor_atual}')
