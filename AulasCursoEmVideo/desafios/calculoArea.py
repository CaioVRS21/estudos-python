def calc(larg, comp):
    area = larg * comp
    return area
print('Controle de terrenos')
print('-'*30)
larg = float(input('Largura(em metros): '))
comp = float(input('Comprimento (em metros): '))
print(f'A área de um terreno de {larg}x{comp} é de {calc(larg, comp)}m²')