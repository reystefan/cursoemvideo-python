def leiaDinheiro(txt):
    while True:
        valor = str(input(txt)).strip()
        if valor.replace(',', '').isnumeric() is False or valor.count(',') > 1:
            print(f'ERRO, {valor} é um preço inválido.')
            continue
        else:
            for carac in valor:
                if carac == ',':
                    valor = valor.replace(',', '.')
            return float(valor)
