elementos = int(input('Digite uma quantidade de elementos: '))
primeiro_elemento = 0
segundo_elemento = 1
prox_elemento = 0
contador = 3
print(f'{primeiro_elemento} → {segundo_elemento} → ', end='')

while contador <= elementos:
    contador += 1
    prox_elemento = primeiro_elemento + segundo_elemento
    print(f'{prox_elemento} → ' if contador <= elementos else f'{prox_elemento} \n', end='')
    primeiro_elemento = segundo_elemento
    segundo_elemento = prox_elemento
