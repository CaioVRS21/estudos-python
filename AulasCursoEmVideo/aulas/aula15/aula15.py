#num = int(input('Digite um número: '))
#c = 0
#result = 0
#while not c == num:
  #  c = c + 1
    #result = c % 2
   # if result == 0:
    #    print('esse {} é par'.format(c), end=' ')
   # elif result != 0:
   #     print('esse é {} impar'.format(c), end=' ')
valor = 1
par = 0
impar = 0
while valor != 0:
  valor = int(input('Digite um valor: '))
  result = valor % 2
  if valor < 0:
      input('ERROR valor inválido tente novamene')
  else:
      if result == 0 and valor != 0:
          par += 1
      elif result !=0 and valor != 0:
          impar += 1
print('Foram {} números pares e {} números impares'.format(par, impar))
print('fim')
