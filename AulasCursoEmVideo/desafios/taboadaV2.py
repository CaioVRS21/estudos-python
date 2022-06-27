#desafio 049
num = int(input('Digite um número inteiro qualquer: '))
for i in range (0, 11):
    result = i * num
    print('{}X{}={}'.format(i, num, result))