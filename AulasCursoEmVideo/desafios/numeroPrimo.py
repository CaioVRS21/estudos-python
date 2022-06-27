# Desafio 52
cont = 0
num = int(input('Digite um número: '))
for i in range(1, num+1):
    print('{} '.format(i))
    result = num % i
    if result == 0:
        cont = cont + 1
print('O valor {} foi divisivel {} vezes!'.format(num, cont))
if cont == 2:
    print('Ele É PRIMO')
else:
    print('Ele NÃO É PRIMO!!!')
