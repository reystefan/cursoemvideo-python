def aumentar(val, taxa, form=False):
    res = val+val*taxa/100
    return res if form is False else formatar(res)


def diminuir(val, taxa, form=False):
    res = val-val*taxa/100
    return res if form is False else formatar(res)


def dobro(val, form=False):
    res = val*2
    return res if form is False else formatar(res)


def metade(val, form=False):
    res = val/2
    return res if form is False else formatar(res)


def formatar(val):
    str_val = f'R${val:.2f}'.replace('.', ',')
    return str_val
    