# Desafio 045
import random
from time import sleep
print('Suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
opcao = int(input('Qual a sua jogada? '))

jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0 , 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O jogador jogou {}'.format(jogadas[opcao]))
print('O computador jogou {}'.format(jogadas[computador]))
if computador == 0: #Computador jogou pedra
    if opcao == 0:
        print('EMPATE!!')
    elif opcao == 1:
        print('JOGADOR VENCE!!')
    elif opcao == 2:
        print('COMPUTADOR VENCE!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #Computador jogou papel
    if opcao == 0:
        print('COMPUTADOR GANHA!!')
    elif opcao == 1:
        print('EMPATE!!')
    elif opcao == 2:
        print('JOGADOR VENCE!!')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:  # Computador jogou tesoura
    if opcao == 0:
        print('JOGADOR GANHA!!')
    elif opcao == 1:
        print('COMPUTADOR GANHA!!')
    elif opcao == 2:
        print('EMPATE!!')
    else:
        print('JOGADA INVÁLIDA')






