numero = int(input('Digite um número: '))
contador = numero
fatorial = 1
calculo = ''

while contador > 0:
    print(contador, end=' x ' if contador != 1 else ' = ')
    fatorial *= contador
    calculo += f'{contador} x ' if contador != 1 else f'{contador} = {fatorial}'
    contador -= 1
    

print(fatorial) # Mostrando o calculo com varios prints em sequencia dentro do while
print(calculo)  # Mostrando o calculo com uma variável string concatenada durante as iterações
