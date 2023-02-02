peso_kg = float(input('Digite o seu peso (Kg): '))
altura_m = float(input('Digite a sua altura (m): '))
imc = peso_kg / altura_m**2

if imc < 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obesidade.')
elif imc > 40:
    print('Obesidade mórbida.')
