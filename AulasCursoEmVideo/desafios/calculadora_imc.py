# Desafio 043
from math import pow
peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em M: '))

imc = peso / pow(altura, 2)
print('Seu imc é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 < imc < 25:
    print('Você está no seu peso ideal')
elif 25 < imc < 30:
    print('Você está com sobrepeso')
elif 30 < imc < 40:
    print('Você está com Obesidade')
else:
    print('Você está com obesidade morbida')
