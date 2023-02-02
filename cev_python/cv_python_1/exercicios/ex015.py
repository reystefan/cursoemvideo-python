km_rodados = float(input('Quantos km foram rodados com o carro? '))
dias_rodados = int(input('Quantos dias rodados? '))
preco = dias_rodados * 60 + km_rodados * 0.15

print(f'Preço do aluguel: R${preco:.2f}')