from math import pow, sqrt, hypot
catopos = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))

hipo = sqrt(pow(catopos, 2) + pow(catadj, 2)) 
hipo2 = hypot(catopos, catadj)
print('O valor da hipotenusa é de {}'.format(hipo2))
