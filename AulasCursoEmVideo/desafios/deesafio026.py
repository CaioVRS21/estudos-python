frase = input('Digite uma frase: ')

print('A frase {}, possui {} letras "a"'.format(frase, frase.count('a')))
print('Ela aparece pela primeira vez no index {}'.format(frase.index('a')))
print('Ela aparece pela ultima vez n index {}'.format(frase.rindex('a')))
