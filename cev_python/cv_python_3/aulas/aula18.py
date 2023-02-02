teste = list()

teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  #  Lembrar de sempre utilizar uma 'cópia' qnd for trabalhar com listas

print(galera)