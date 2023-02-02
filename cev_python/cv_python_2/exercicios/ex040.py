import numpy
nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
media = (nota_1 + nota_2) / 2
media = numpy.around(media, 1)

if media < 5:
    print(f'Média: {media}. REPROVADO.')
elif media >= 5 and media <= 6.9:
    print(f'Média: {media}. RECUPERAÇÃO.')
elif media >= 7:
    print(f'Média: {media}. APROVADO.')

