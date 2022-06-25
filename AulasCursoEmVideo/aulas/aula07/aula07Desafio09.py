num = int(input('Digite um número e veja sua taboada: '))

for i in range (0, 11):
    result = i * num
    print('{}X{} = {}'.format(num, i, result))
