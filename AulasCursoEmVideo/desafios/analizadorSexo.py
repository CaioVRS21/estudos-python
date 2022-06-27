# Desafio 057
sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = input('Digite seu sexo[M/F]: ').strip().upper()
    if sexo == 'M':
        print('Você é homem')
        break
    elif sexo == 'F':
        print('Você é mulher')
        break
    else:
        print('Valor inválido tente novamente')
print('Fim')
