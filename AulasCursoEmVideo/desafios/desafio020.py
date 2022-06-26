import random
print('Veremos agora a ordem de quem vai apresentar primeiro, digite abaixo os nomes dos membros do grupo')
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segubdo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

listaNome = [nome1, nome2, nome3, nome4]

random.shuffle(listaNome)

print('A ordem de apresentação é: {}'.format(listaNome))