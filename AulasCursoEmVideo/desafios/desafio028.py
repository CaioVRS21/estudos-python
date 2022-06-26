import random
print('Estou pensando em um número, advinhe qual é!')
num = int(input('Digite um número entre 0 e 5: '))
numPc = int(random.randrange(0, 5))

if num > 5:
    print('Epa! Somente números entre 0 e 5 são válidos! Tente denovo')
if num == numPc:
    print('Quem diria você acertou! Estava justamente pensando em {}'.format(numPc))
else:
    print('Mais sorte na próxima! Estava pensanado em {}, e você chutou {}'.format(numPc, num))