nome = input('Digite seu nome: ').strip() # Remove espaços inuteis do inicio e do fim

print(nome.upper())
print(nome.lower())
print(len(''.join(nome.split()))) # Separa a string onde ha espaços e depois 
                                  #junta tudo apenas para contar
print(len(nome)-nome.count(' '))  # Comprimento do nome MENOS os espaços contidos em nome


#print(nome.find' ') # Retorna o valor do indice anterior ao primeiro espaço
nome_separado = nome.split()[0]
print(len(nome_separado))

print(len(nome.split()[0]))

print(nome.find(' ')) # Retorna o indice anterior ao primeiro espaço, que coincide
                      # com a quantidade de letras do primeiro nome
                      # porém so funciona se a pessoa digitar mais de um nome para
                      # que assim haja um espaço na string, caso contrário, o find()
                      # não encontrará nenhum espaço e retornará -1.