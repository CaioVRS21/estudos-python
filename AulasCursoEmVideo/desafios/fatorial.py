def fatorial(num=1, show=False):
    """
    Calcula o fatorial de um número
    num: O número que será calculado
    show: (Opcional) mostra o calculo completo ou não
    return: retorna o valor do fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} X', end=' ')
            else:
                print(f'{c} =', end=' ')
    return f' {f}'
n = int(input('Digite um número: '))
print(fatorial(n, show=False))
help(fatorial)