velocidade = int(input('Velocidade do carro: '))
multa = ((velocidade - 80) * 7.00) if velocidade > 80 else None

if velocidade > 80:
    print(f'MULTADO! Você ultrapassou o limite de 80km/h e foi multado em R${multa:.2f}')
else:
    print('Dirija com segurança!')