lista = []

while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já adicionado, ele não será repetido')
    continuar = str(input('Quer continuar?[S/N]: '))
    if continuar.upper() == 'N':
        break;
lista.sort()
print(f'Você digitou: {lista}')
