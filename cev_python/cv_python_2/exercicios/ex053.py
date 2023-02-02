frase = input('Digite uma frase: ').strip().upper()
frase_normal_sem_espaco = ''.join(frase.split())
frase_invertida = ''

for letra in range(len(frase_normal_sem_espaco) - 1, -1, -1):
    frase_invertida += frase_normal_sem_espaco[letra]

print(f'A frase {frase} sem espaços é {frase_normal_sem_espaco}'
    f' e ao contrário é {frase_invertida}.')

if frase_invertida == frase_normal_sem_espaco:
    print('Portanto, É PALÍNDROMO!')
else:
    print('Portanto, NÃO É PALÍNDROMO!')
    

