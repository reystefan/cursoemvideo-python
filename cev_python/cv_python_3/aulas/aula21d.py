def funcao():
    n1 = 4
    print(f'N1 dentro(local) vale {n1}')


n1 = 2
funcao()
print(f'N1 fora(global) vale {n1}')