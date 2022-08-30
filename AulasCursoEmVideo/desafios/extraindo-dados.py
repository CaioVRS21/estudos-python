lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    decisao = str(input('Quer continuar?[S/N]: '))
    if decisao in 'Nn':
        break;

print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse = True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print('O valor 5 não faz parte da lista')
else:
    print('O valor 5 faz parte da lista')