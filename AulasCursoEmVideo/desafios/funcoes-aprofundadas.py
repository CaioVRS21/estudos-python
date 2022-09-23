def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por Favor digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! Entrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar nenhum valor\033[m')
            return 0
        else:
            return n

num = LeiaInt('Digite um valor inteiro: ')
num2 = LeiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num}')
print(f'O valor real digitado foi {num2}')
