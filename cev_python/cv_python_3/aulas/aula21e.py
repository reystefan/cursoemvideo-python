#  Como utilizar a variável global dentro da função

def teste(b):
    global a  # Informa ao programa para utilizar a variável global ao invés de criar uma variável 'a' local
    a = 8      
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')  #  Nota: mesmo que 'a' tenha sido inicializada com valor 5
                           # no escopo global, a função teste é chamada depois dessa inicialização
                           # e executada, fazendo com que então 'a' global receba o valor '8'
                           # apenas NESSE CASO.