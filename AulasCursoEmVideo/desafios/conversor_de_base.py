# Desafio 037
num = int(input('Digite um número inteiro qualquer: '))
print('Escolha uma das bases númericas para converter')
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXA')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(format(num, 'b'))
elif opcao == 2:
    print(format(num, 'o'))
elif opcao == 3:
    print(format(num, 'x'))
else:
    print('Valor inválido! Tente novamente')


