numero = qtd_numero = soma = 0

while numero != 999:
    soma += numero
    numero = int(input('Digite um número: '))
    if numero != 999:
        qtd_numero += 1
    else:
        print('Finalizando. . .')
    

print(f'{qtd_numero} foram digitados e a soma entre eles é {soma}')