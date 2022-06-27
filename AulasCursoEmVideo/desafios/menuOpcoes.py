#desafio 59
from time import sleep
num = float(input('Primeiro Valor: '))
num2 = float(input('Segundo Valor: '))
opcao = 0
while opcao != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do programa')
    opcao = int(input('Qual sua escolha? '))

    print('PENSAND0...')
    sleep(3)

    if opcao == 1:
        print('Você escolheu {}'.format(opcao))
        result = num + num2
        print('O resultado da soma é {}'.format(result))
        sleep(3)
    elif opcao == 2:
        print('Você escolheu {}'.format(opcao))
        result = num * num2
        print('O resultado da mulplicação é {}'.format(result))
        sleep(3)
    elif opcao == 3:
        print('Você escolheu {}'.format(opcao))
        if num > num2:
            print('O maior valor é {}'.format(num))
            sleep(3)
        elif num < num2:
            print('O maior valor é {}'. format(num2))
            sleep(3)
        else:
            print('Os valores são iguais')
            sleep(3)
    elif opcao == 4:
        print('Você escolheu {}'.format(opcao))
        num = float(input('Digite um número qualquer: '))
        num2 = float(input('Digite um número qualquer: '))
    elif opcao == 5:
        print('Você escolheu {}'.format(opcao))
    else:
        print('Valor inválido tente novamente')
print('Fim do programa')

