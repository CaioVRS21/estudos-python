from random import randint
valores = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))
print(f'Os valores sorteados foram {valores}')
print(f'O maior valor é: {max(valores)}')
print(f'O menor valor é: {min(valores)}')