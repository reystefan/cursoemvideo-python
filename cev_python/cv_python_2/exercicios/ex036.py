valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos_parcela = int(input('Em quantos anos será pago: '))
qtd_meses = anos_parcela * 12
valor_prestacao = None

if valor_casa / qtd_meses <= 0.3 * salario:
    valor_prestacao = valor_casa / qtd_meses
    print(f"""Parabéns! Seu empréstimo de R${valor_casa:.2f} foi aprovado! A parcela será de
    R${valor_prestacao:.2f} em um total de {qtd_meses} parcelas.""")
else:
    print('Infelizmente seu empréstimo não foi aprovado.')