#desafio 041
from datetime import  date
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif 9 < idade <= 14:
    print('Classificação: INFANTIL')
elif 14 < idade <= 19:
    print('Classificação: JUNIOR')
elif 19 < idade < 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
