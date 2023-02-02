palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
             'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 
             'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print(f'Palavra: {palavra} tem as seguintes vogais: ', end='')
    for vogal in vogais:
        if vogal in palavra:
            print(vogal, end=' ')
    print('\n')

#ou

for palavra in palavras:
    print(f'Palavra: {palavra} tem as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('\n')