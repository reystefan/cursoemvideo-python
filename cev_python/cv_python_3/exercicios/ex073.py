times = ('Palmeiras', 'Flamengo', 'Internacional', 'Gremio', 'São Paulo',\
        'Atletico-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos',\
        'Bahia', 'Fluminense', 'Corinthians',\
        'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'América-MG',\
        'EC Vitória', 'Paraná')

print(f'Cinco primeiros: {times[0:5]}\n')

print(f'Quatro últimos: {times[-4:]}\n')
print(f'{times[16:]}\n')

times_ordem = sorted(times)
print(times_ordem, '\n')

print(f'Chapecoense está na posição {times.index("Chapecoense") + 1}')