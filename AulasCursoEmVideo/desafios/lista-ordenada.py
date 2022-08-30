lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]: #Para inserir o primeiro valor ou adicionar um novo último valorcaso este seja maior que o último valor original
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]: #se o valor inserido for menor do que o que já está na posição pos então a posição pos recebe este novo valor
                lista.insert(pos, n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break;
            pos+=1
print('-='*30)
print(f'O valors digitados foram {lista}')
