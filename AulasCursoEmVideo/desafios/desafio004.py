algo = input('Digite algo: ')

print('O tipo prmimitivo desse valor é: {}'.format(type(algo)))
print('Só tem espaços? {}'.format(algo.isspace()))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanúmerico? {}'.format(algo.isalpha()))
print('Está em maiúsculas? {}'.format(algo.isupper()))
print('Está em minúsculas? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.istitle()))

