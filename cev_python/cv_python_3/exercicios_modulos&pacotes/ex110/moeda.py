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

def resumo(val, taxa_aum=0, taxa_dim=0):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analisado: ":<29}{formatar(val)}')
    print(f'{"Dobro do preço: ":<29}{formatar(dobro(val))}')
    print(f'{"Metade do preço: ":<29}{formatar(metade(val))}')
    if taxa_aum != 0:
        print(f'{f"{taxa_aum}% de aumento: ":<29}{formatar(aumentar(val, taxa_aum))}')
    if taxa_dim != 0:
        print(f'{f"{taxa_dim}% de redução: ":<29}{formatar(diminuir(val, taxa_dim))}')
    print('-'*40)
    