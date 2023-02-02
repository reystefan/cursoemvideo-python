# pessoas = dict()
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())

for k, v in pessoas.items():
    print(k, v)

# del pessoas['sexo']  # Apaga a chave sexo e seus valores

pessoas['nome'] = 'Leandro'  #  Altera
pessoas['peso'] = 98.5       #  Adiciona