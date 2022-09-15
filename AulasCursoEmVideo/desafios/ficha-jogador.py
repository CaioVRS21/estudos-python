def ficha(nome, gols=0):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome.strip() == '':
        nome = "<desconhecido>"
    else:
        nome = str(nome)
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'
nome = str(input('Digite o nome do jogador: '))
gols = input('Quantos gols ele fez no campeonato: ')
print(ficha(nome, gols))