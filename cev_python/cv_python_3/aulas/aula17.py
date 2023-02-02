#  Listas

# São como tuplas, porém são imutáveis.

# Possui comandos diferentes

lanche = ['Hamburguer', 'Suco','Pizza', 'Pudim']
print(lanche)
lanche[3] = 'Picole' #  Substitui valores dentro do índice (key) indicado

lanche.append('Cookie')  # Adiciona um elemento ao final da lista.
print(lanche)

lanche.insert(0, 'Cachorro-quente')  #  Cria uma nova chave 0 e "empurra" as outras
                                     # chaves pra + 1 posicão
print(lanche)

del lanche[3] # Comando
lanche.pop(3) # Método: normalmente utilizado para eliminar a ultima chave, mas tbm pode eliminar a chave passada pelo parametro
lanche.remove('Pizza') # Remove a chave que possui o conteudo indicado no parametro
# Em todos os casos o índice 3 = Pizza será eliminado nesse caso.

lanche.pop() # Elimina o último elemento

if 'Pizza' in lanche:           # Verifica se o conteudo existe na lista e o elimina caso exista
    lanche.remove('Pizza')

valores = list(range(4, 11))  # Cria uma lista a partir de uma contagem de 4 a 10
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()  # Ordena todos os valores

valores.sort(reverse=True)  # Ordena na ordem inversa (reversa)


