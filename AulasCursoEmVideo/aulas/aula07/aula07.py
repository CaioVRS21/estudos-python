num1 = int(input('Digite o valor nº1: '))
num2 = int(input('Digite o valor nº2: '))

soma = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2
divInt = num1 // num2
divRest = num1 % num2
pot = num1 ** num2

print('Os valores digitados foram {} e {}, a soma dos dois é {}, sua subtração é {}, sua multiplicação é {} e sua divisão {}, a divisão interia deles e o resto da divisão, são de respectivamente {} e {} e a potenciação dos dois é {}'.format(num1, num2, soma, sub, multi, div, divInt, divRest, pot))


