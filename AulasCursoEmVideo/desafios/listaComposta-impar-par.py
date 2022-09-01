valores = [[], []]
for i in range(1,8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
if len(valores[0]) == 0:
    print('Nenhum valor par foi digtado')
else:
    print(f'Os valores par são {valores[0]}')
if len(valores[1]) == 0:
    print('Nenhum valor impar foi digitado')
else:
    print(f'Os valores impar são {valores[1]}')