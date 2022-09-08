jogadores = []
jogador = {}
gols = []
soma = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(partidas):
        gol = int(input(f'Quantos gols ele fez no jogo {i+1}? '))
        gols.append(gol)
        soma += gol
    jogador['gols'] = gols[:]
    jogador['total de gols'] = soma
    jogadores.append(jogador.copy())
    soma = 0
    gols.clear()
    while True:
        decisao = str(input('Deseja continuar?[S/N]')).upper()[0]
        if decisao in 'SN':
            break
        print('Valor inválido tente novamente')
    if decisao == 'N':
        break
print('-='*35)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*35)
for k, v in enumerate(jogadores):
    print(f'{k:>2} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*35)
while True:
    dados = int(input('Deseja ver os dados de qual Jogador?(999 para parar) '))
    if dados == 999:
        print('--- FIM ---')
        break
    if dados >= len(jogadores):
        print(f'ERROR! Não existe jogador com código {dados}')
    else:
        print(f'--- LEVANTAMENTO DE DADOS DO JOGADOR {jogadores[dados]["nome"]}')
        for i, g in enumerate(jogadores[dados]['gols']):
            print(f'No jogo {i+1} fez {g} gols!')
print('-'*30)