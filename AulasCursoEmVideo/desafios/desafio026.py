frase = input('Digite uma frase: ').lower().strip()

print('A frase {}, possui {} letras "a"'.format(frase, frase.count('a')))
print('Ela aparece pela primeira vez no index {}'.format(frase.index('a')+1))
print('Ela aparece pela ultima vez n index {}'.format(frase.rfind('a')+1))
