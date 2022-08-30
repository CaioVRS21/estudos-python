lista = []
pares = []
impares = []

while True:
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    decisao = str(input('Deseja continuar?[S/N]: '))
    if decisao in 'Nn':
        break;
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(f'A lista completa é {lista}')
if len(pares) == 0:
    print('A lista não possuí valores pares')
else:
    print(f'Os valores pares dentro da lista são {pares}')

if len(impares) == 0:
    print('A lista não possuí valores impares')
else:
    print(f'Os valores impares dentro da lista são {impares}')
