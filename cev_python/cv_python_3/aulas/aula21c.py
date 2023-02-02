def somar(a=0, b=0, c=0):  #  Parâmetros opcionais, são valores atribuidos aos parametros de forma padrão, caso o programa não passe um parâmetro
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor

    '''
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()