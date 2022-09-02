from random import randint
from time import  sleep
from operator import itemgetter
jogadores = {
    'Jogador1:': randint(1, 9),
    'Jogador2:': randint(1, 9),
    'Jogador3:': randint(1, 9),
    'Jogador4:': randint(1, 9)
}
ranking = []
for k, v in jogadores.items():
    print(f'{k} jogou {v} no dado')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse = True)
print('-='*20)
print('=== RANKING DOS JOGADORES ===')
for i,v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
