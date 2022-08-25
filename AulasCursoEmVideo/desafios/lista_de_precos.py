itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Tranferidor', 4.2, 'Compasso', 9.9, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print("-"*40)
print(f"{'LISTAGEM DE PREÇO' : ^40}")
print("-"*40)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')

