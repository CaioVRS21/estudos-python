print('Quer saber se um ano é ou não bissexto?')
ano = int(input('Digite um ano: '))

if (ano % 100 == 0) and (ano % 400 == 0):
    print('O ano {} é um ano bissexto'.format(ano))
if (ano % 4 == 0) and (ano % 100 != 0):
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {}, não é um ano bissexto'.format(ano))
