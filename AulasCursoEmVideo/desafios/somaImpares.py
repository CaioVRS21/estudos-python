# desafio 48
soma = 0
contador = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador = contador + 1
        soma = soma + i
print('A soma de todos os valores é {} e o total de valores é {}'.format(soma, contador))
