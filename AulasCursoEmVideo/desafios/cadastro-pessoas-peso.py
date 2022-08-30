pessoa = list()
pessoas = list()
maior = menor = 0

while True:
    pessoa.append(str(input('Digite um nome: ')))
    pessoa.append(int(input('Digite um peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear() #para limpar os dados inseridos a cada laço
    decisao = str(input('Deseja continuar?[S/N]: '))
    if decisao in 'Nn':
        break;

print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'Os maiores pessos são ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'\nOs menores pessos são ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
