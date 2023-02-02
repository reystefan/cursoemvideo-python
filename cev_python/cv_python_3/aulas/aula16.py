#    Tuplas

#Tuplas sao IMUTÁVEIS

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')  # Tbm pode ser criado sem parenteses

for comida in lanche:
    print(f'Eu comi {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')
    
print('Comi pra caramba!')

print(sorted(lanche))
print(lanche)
