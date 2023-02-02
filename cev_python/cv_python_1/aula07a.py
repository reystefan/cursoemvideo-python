numero = 3**2
print(numero)

numero_2 = pow(3,2)
print(numero_2)

nome = input('Qual o seu nome? ')

print(f'Prazer em te conhecer {nome:=^20}!')

num_1 = int(input('Digite um valor: '))
num_2 = int(input('Outro valor: '))

s = num_1 + num_2
m = num_1 * num_2
d = num_1 / num_2
di = num_1 // num_2
e = num_1 ** num_2

print(f'A sooma é {s}, o produto é {m}, a divisão é {d:.3f}, '
f'a divisão inteira é {di} e a exponenciação é {e}', end=' >>> ')

print('A soma é {}, o produto é {}, a divisão é {}, '
'a divisão inteira é {} e a exponenciação é {}'.format(s, m, d, di, e))