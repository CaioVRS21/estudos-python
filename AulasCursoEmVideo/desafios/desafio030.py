num = int(input('Digite um número inteiro para saber se ele é par ou ímpar: '))
result = num % 2

if result == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))