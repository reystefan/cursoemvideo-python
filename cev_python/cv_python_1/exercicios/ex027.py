nome = input('Digite seu nome completo: ').strip().title()
nome_separado = nome.split()

print(f"""Seu primeiro nome é: {nome_separado[0]}
Seu último nome é: {nome_separado[-1]}""")

#ou
print(f'Seu último nome é: {nome_separado[len(nome_separado) - 1]}')
#--------IMPORTANTE: O método len() não começa a contagem com 0