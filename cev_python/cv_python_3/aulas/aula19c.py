estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())  #  Cria uma cópia dos dados do dicionário para q nao haja uma relação entre eles

for e in brasil:  # para cada estado (dicionario) dentro da lista brasil
    for k, v in e.items():  #  para cada chave e valor dentro do dicionario 'e' (que será o dicionario 'estado')
        print(f'O campo {k} tem valor{v}')  # mostra as chaves e os valores de cada chave
    
    for v in e.values():
        print(v, end=' ')  #  Mostra apenas todos os valores contidos no dicionário, sem as suas chaves