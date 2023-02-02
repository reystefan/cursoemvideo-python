numero_1 = int(input('Digite o 1 número: '))
numero_2 = int(input('Digite o 2 número: '))
numero_3 = int(input('Digite o 3 número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'Numero {numero_1} é o maior!')
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'Numero {numero_2} é o maior!')
else:
    print(f'Numero {numero_3} é o maior!')

    #ou

menor = numero_1

if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

print(f'O menor número é o {menor}')
        
        
