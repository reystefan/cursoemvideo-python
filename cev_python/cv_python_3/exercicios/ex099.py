def maior(* valores):
    print('-=' * 30)
    maior_valor = 0
    for pos, n in enumerate(valores):
        print(n, end=' ')
        if pos == 0 or n > maior_valor:
            maior_valor = n
        
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

