valor = int(input('Digite o valor a ser sacado: R$'))
tot_valor = valor
tot_cedulas = 0
valor_cedula = 50

while True:
    if tot_valor >= valor_cedula:
        tot_cedulas = tot_valor // valor_cedula
        tot_valor = tot_valor % valor_cedula
        print(f'Total de {tot_cedulas} cédulas de R${valor_cedula}.')
    
    elif tot_valor >= 20:
        valor_cedula = 20
    elif tot_valor >= 10:
        valor_cedula = 10
    elif tot_valor >= 1:
        valor_cedula = 1

    if tot_valor == 0: 
        break