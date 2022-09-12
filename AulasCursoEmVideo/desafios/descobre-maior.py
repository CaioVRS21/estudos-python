def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    maior = contador = 0
    for v in num:
        print(f'{v}', end=' ', flush=True)
        if contador == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        contador += 1
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {maior}')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)

