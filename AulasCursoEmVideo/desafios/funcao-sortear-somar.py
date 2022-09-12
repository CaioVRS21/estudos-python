from random import randint
from time import sleep
valores = []
def sorteio (lista):
    print('Sorteando 5 valores da lista')
    for count in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(0.3)
    print('PRONTO')
def soma(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os números pares de {lista} temos {soma}')
sorteio(valores)
soma(valores)
