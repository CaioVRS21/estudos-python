import random
nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segubdo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

listaNome = [nome1, nome2, nome3, nome4]

nomeAlea = random.choice(listaNome)

print('O aluno ou aluna escolhida para limpar o quadro foi: {}'.format(nomeAlea))
