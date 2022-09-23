try:
    a = input('Digite o primeiro valor: ')
    b = input('Digite o segundo valor: ')
    r = a/b
    print(r)
except TypeError:
    print('ERRO! Use apenas números!')
except ValueError:
    print('ERRO! Valor inválido!')
except ZeroDivisionError:
    print('ERRO! Matematicamente é impossível dividir um número por zero')
