soma = qtd_numeros = 0

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    else: 
        qtd_numeros += 1
        soma += numero

print(f'{qtd_numeros} números foram digitados e a soma entre eles foi {soma}')