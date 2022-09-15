#docstrings
def contador(i, f, p):
    #docscrtings são a forma do desenvolvedor criar um manual explicando como funciona suas funções
    """
    i = ínicio da contagem
    f = fim da contagem
    p = passo da contagem
    """
    c = i
    while c < f:
        print(f'{c}')
        c += p
    print('FIM!')
#help(contador)

def somar (a, b, c = 0): #Caso 'c' não receba nenhum valor em sua chamada, ele possui o parâmetro opcional de "0"
    s = a+b+c
    print(f'A soma é {s}')
#somar(1,5)

def fatorial (num = 1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
#n = int(input('Digite um número: '))
#print(f'o fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'{f1}, {f2}, {f3}')