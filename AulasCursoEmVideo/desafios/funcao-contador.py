from time import sleep
def conta():
    contador = 0
    contador2 = 0
    print('-=' * 30)
    print('Contar de 0 a 10 de 1 em 1')
    print('-=' * 30)
    while contador <= 10:
        sleep(1)
        print(contador, end=' ')
        contador += 1
    print('FIM!')
    sleep(1)
    print('-='*30)
    print('Contar de 0 a 10 de 2 em 2')
    print('-='*30)
    while contador2 <=10:
        sleep(1)
        print(contador2, end=' ')
        contador2 += 2
    print('FIM!')
    print('Agora é sua vez de personalizar a contagem')
    inicio = int(input('Ínicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio > fim:
        while inicio >= fim:
            sleep(1)
            print(inicio, end=' ')
            inicio -= passo
    elif inicio < fim:
        while inicio <= fim:
            sleep(1)
            print(inicio, end=' ')
            inicio += passo

conta()