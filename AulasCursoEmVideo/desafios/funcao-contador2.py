from time import sleep
def conta (i, f, p):
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    print('-='*30)
    if p == 0:
        p == 1
    if i > f:
        while i >= f:
            sleep(1)
            print(i, end=' ')
            i -= p
    elif i < f:
        while i <= f:
            sleep(1)
            print(i, end=' ')
            i += p
    print('FIM!')
conta(0, 10, 1)
conta(0, 10, 2)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
conta(i, f, p)
