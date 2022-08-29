valores = []
min = 0
max = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        min = max = valores[c]
    else:
        if valores[c] > max:
            max = valores[c]
        if valores[c] < min:
            min = valores[c]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max} na posição ', end='')
for i, v in enumerate(valores):
    if v == max:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min} na posição ', end='')
for i, v in enumerate(valores):
    if v == min:
        print(f'{i}...', end = '')
print()

