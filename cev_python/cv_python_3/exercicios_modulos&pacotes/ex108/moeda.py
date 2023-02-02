def aumentar(val, taxa):
    res = val+val*taxa/100
    return res


def diminuir(val, taxa):
    res = val-val*taxa/100
    return res


def dobro(val):
    res = val*2
    return res


def metade(val):
    res = val/2
    return res


def formatar(val):
    str_val = f'R${val:.2f}'.replace('.', ',')
    return str_val
