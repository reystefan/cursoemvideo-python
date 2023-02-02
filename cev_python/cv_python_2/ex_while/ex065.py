maior_valor = menor_valor = soma = contagem = 0
continuar = 'S'

while continuar == 'S':
    numero = int(input('Digite um número: '))
    soma += numero

    if contagem == 0:
        maior_valor = numero
        menor_valor = numero
    else:
        if numero < menor_valor:
            menor_valor = numero
        elif numero > maior_valor:
            maior_valor = numero
        else:
            maior_valor = numero
            menor_valor = numero

    continuar = input('Quer continuar? (S ou N): ').strip().upper()[0]
    contagem += 1

media = soma / contagem
print(f'A média de todos os valores foi: {media}')
print(f'Soma total = {soma}')
print(f'O maior número foi {maior_valor} e o menor foi {menor_valor}')