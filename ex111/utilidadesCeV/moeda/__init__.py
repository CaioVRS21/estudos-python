def metade(num=0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if formato is False else moeda(res)


def aumento(num=0, taxa=0, formato=False):
    res = num + (num * (taxa/100))
    return res if formato is False else moeda(res)


def diminuir (num=0, taxa=0, formato=False):
    res = num - (num * taxa/100)
    return res if formato is False else moeda(res)


def moeda (num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num=10, txaut=10, txdim=5):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'O dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{txaut}% de aumento: \t{aumento(num, txaut, True)}')
    print(f'{txdim}% de redução: \t{diminuir(num, txdim, True)}')
    print('-'*30)


