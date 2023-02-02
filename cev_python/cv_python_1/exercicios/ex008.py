distancia_metros = float(input('Uma distância em metros: '))
km = distancia_metros/1000
hm = distancia_metros/100
dam = distancia_metros/10
dm = distancia_metros*10
cm = distancia_metros*100
mm = distancia_metros*1000

print(f'A medida de {distancia_metros}m corresponde a \n'
f'{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')