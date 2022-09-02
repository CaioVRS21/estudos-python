jogador = {}
gols = []
soma = 0
jogador['nome'] = str(input('Qual o nome deste jogador? '))
partidas = int(input('Quantas paartidas ele jogou? '))
for p in range(1, partidas+1):
    gol = int(input(f'Quantos gols ele marcou na partida {p}? '))
    gols.append(gol)
    soma += gol
jogador['gols'] = gols[:]
jogador['total de gols'] = soma
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for p in range(1, partidas+1):
    print(f'=> Na partida {p}, fez {gols[p-1]} gols')
print(f'Foi um total de {soma} gols!')