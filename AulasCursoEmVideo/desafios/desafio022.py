nome = input('Digite seu nome: ')

print('Seu nome com todas as letras maiúsculas fica {}'.format(nome.upper()))
print('seu nome com todas as letras minúsculas fica {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
