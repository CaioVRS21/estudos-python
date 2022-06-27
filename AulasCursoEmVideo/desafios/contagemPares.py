#Desafio 047
soma = 0
contador = 0
for i in range(1, 7):
    num = int(input('Digite um número inteiro qualquer: '))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
if contador > 1:
    print('A soma dos {} números pares é de {}'.format(contador, soma))
else:
    print('Há somente um número par, o número {}'.format(soma))
