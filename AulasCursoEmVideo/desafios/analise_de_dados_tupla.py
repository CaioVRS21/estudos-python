valores = (
int(input('Digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('Digite o último valor: ')),
)
pares = []
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if valores.__contains__(3):
    print(f'O primeiro número 3 apareceu na posição {valores.index(3)+1}')
else:
    print('O número 3 não apareceu nenhuma vez')
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(f'O total de números pares digitados foi {len(pares)}')
