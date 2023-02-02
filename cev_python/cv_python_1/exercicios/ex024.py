cidade = input('Qual a dua cidade? ').strip().title()
cidade_separado = cidade.split()

print(cidade_separado)
print(cidade_separado[0])
print('Santo' in cidade_separado[0]) # Começa com Santo

#Ou
print(cidade[:5] == 'Santo')

