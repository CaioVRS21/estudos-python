times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'EC Vitória', 'Curitiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print("-="*len(times))
print(f'Lista de times do Brasileirão: {times}')
print("-="*len(times))
print(f'Os 5 primeiros são: {times[0:5]}')
print("-="*len(times))
print(f'Os 4 últimos são {times[-4:]}')
print("-="*len(times))
print(f'Os times em ordem alfabética: {sorted(times)}')
print("-="*len(times))

for pos, time in enumerate(times):
    pos += 1
    if time == 'Chapecoense':
        print(f'O {time} está na {pos}ª posição')

