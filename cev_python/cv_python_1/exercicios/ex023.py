numero = input('Digite um número: ')
numero_int = int(numero)

# print(f""" Unidade: {numero[3]}
#  Dezena: {numero[2]} 
#  Centena: {numero[1]} 
#  Milhar: {numero[0]}\n""")             ## Dá erro quando nao se usam os 4 digitos

# milhar = int(numero[0])
# centena = int(numero[1])
# dezena = int(numero[2])
# unidade = int(numero[3])
# print(milhar, centena, dezena, unidade)

unidade_2 = numero_int // 1 % 10
dezena_2 = numero_int // 10 % 10
centena_2 = numero_int // 100 % 10
milhar_2 = numero_int // 1000 % 10

print('Fatiando o número de forma matemática:', unidade_2, dezena_2, centena_2, milhar_2)





