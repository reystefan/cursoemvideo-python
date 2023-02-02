# Fatiamento
frase = 'Curso em Vídeo Python'

print('-'*14, 'Fatiamento', '-'*14)

print(frase[9]) # V
print(frase[9:13]) # Víde
print(frase[9:21]) # Vídeo Python 
print(frase[9:21:2]) # VdoPto
print(frase[:5]) # Curso
print(frase[15:])
print(frase[9::3])

#Análise
print('-'*14, 'Analise', '-'*14)

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13)) # Contagem com fatiamento
print(frase.find('deo'))
print(frase.find('Android'))  # Retorna -1 quando a string procurada nao existe
print('Curso' in frase)  # Mostra em bool se a string existe

#Transformação
print('-'*14, 'Transformação', '-'*14)

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())  # Somente a primeira letra da string em maiuscula
print(frase.title()) # Primeira letra de cada palavra em maiúscula

frase = '   Aprenda Python  '
print(frase.strip()) # Remove espaços inuteis
print(frase.rstrip()) # Esquerda
print(frase.lstrip()) # Direita

# Divisão
print('-'*14, 'Divisão', '-'*14)

frase = 'Curso em Vídeo Python'

print(frase.split()) # Divide as palavras nos espaços e as coloca em uma lista

# Junção
print('-'*14, 'Junção', '-'*14)

frase_separada = frase.split()
print(frase_separada)
print('-'.join(frase_separada))



















