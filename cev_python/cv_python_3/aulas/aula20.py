def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma é {s}\n')


soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)

soma(a=5, b=4)  #  É possível ser explicito ao informar os parametros
soma(b=4, a=5)  #  Dessa forma, a ordem não influencia

soma(3, b=7)
soma(a=3, b=7)  # A partir do momento em q vc é explicito em algum parametro, todos os parametros seguintes
                # também devem ser explícitos, com exceção apenas dos anteriores.