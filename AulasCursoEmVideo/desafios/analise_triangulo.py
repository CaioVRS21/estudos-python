#desafio 042
print('Vamos descobrir se podemos ou não formar um triângulo')
reta1 = float(input('Digite o valor da primeira reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite o valor da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível montar um triângulo!')
    if reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print('Este é um triângulo equilátero')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Este triângulo é isósceles')
    else:
        print('Este é um triângulo escaleno')
else:
    print('Não é possível montar um triângulo')


