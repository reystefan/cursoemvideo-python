def fatorial(num, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o passo a passo do calculo.
    :return: O valor do Fatorial de um número num.
    '''
    fat = 1
    for n in range(num, 0,  -1):
        fat *= n
        if show:
            print(n, end=' x ' if n != 1 else f' = {fat}')
    print()
    
    return fat

numero = int(input('Digite um número: '))
mostrar = bool(input('Quer mostrar o calculo? (Vazio para "Não") '))
resultado = fatorial(numero, mostrar)

print(resultado)

help(fatorial)

