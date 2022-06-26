nome = input('Digite seu nome: ').strip()
nome2 = nome.split()
print('Seu nome é {}, o seu primeiro nome é {} e seu último nome é {}'.format(nome, nome2[0], nome2[len(nome2)-1]))
