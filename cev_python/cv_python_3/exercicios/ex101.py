def voto(ano):
    from datetime import date  # A importação fica somente dentro da função, o que economiza memória
    idade = date.today().year - ano

    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'

print(voto(2006))