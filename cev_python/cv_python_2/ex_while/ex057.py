sexo = ''

while 'F' != sexo != 'M':
    sexo = input('Informe o seu sexo: ').strip().upper()[0]
    if 'F' != sexo != 'M':
        print(f'Dados inválidos. "{sexo}" não é reconhecido como uma informação de sexo válida. Apenas "M" ou "F".')
    else:
        print(f'Sexo {sexo} registrado com sucesso.')