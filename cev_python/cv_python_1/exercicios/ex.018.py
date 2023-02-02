from math import sin, cos, radians
angulo = float(input('Digite um ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))

print(f'{seno=} {cosseno=}')