#       Empacotar parâmentros

def contador(*num):   # Desempacotar, permite a passagem de varios parametros, sem uma qtd definida
    for valor in num:   # Desempacotamento gera uma tupla com os parametros que foram passados
        print(valor, end='')
    print('\nFIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2) 


def contador(*num):   # Desempacotar, permite a passagem de varios parametros, sem uma qtd definida
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2) 