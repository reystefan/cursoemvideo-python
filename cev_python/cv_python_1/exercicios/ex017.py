import math
cateto_op = float(input('Cateto oposto: '))
cateto_ad = float(input('Cateto adjacente: '))
hipotenusa = math.hypot(cateto_op, cateto_ad)

print(hipotenusa)