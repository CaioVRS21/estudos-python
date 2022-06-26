#Desafio 039
import datetime
anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNasc
alista = 18 - idade
dataAlista = anoAtual + alista
alistaAtraso = idade - 18
anoAtraso = anoAtual - alistaAtraso

print('Você tem {} anos'.format(idade))

if idade < 18:
    print('faltam {} anos para o seu alistamento e você vai se alistar em {}'. format(alista, dataAlista))
elif idade == 18:
    print('Você já tem 18, apresente-se o mais cedo possível a um centro de alistamento')
else:
    print('Seu alistamento deveria ter sido há {} anos atrás e deveria ter se alistado em {} vá logo caso não queria ter problemas'.format(alistaAtraso, anoAtraso))

