reta_1 = int(input('Quanto mede a 1 reta? '))
reta_2 = int(input('Quanto mede a 2 reta? '))
reta_3 = int(input('Quanto mede a 3 reta? '))

triangulo_existe = (reta_1 + reta_2) > reta_3 and (reta_1 + reta_3) > reta_2 and \
                    (reta_3 + reta_2) > reta_1
equilatero = reta_1 == reta_2 == reta_3

if triangulo_existe:
    if reta_1 == reta_2 == reta_3:
        print('Com essas retas é possível formar um triângulo EQUILÁTERO!')
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print('Com essas retas é possível formar um triângulo ESCALENO!')
    else:
        print('Com essas retas é possível formar um triângulo ISÓSCELES!')

else:
    print('Não é possível formar um triângulo!')
