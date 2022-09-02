pessoa = {}
pessoas = []
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo:[M/F] ')).upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('Valor inválido! Tente novamente')
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        decisao = str(input('Deseja continuar?[S/N]')).upper()
        if decisao in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if decisao == 'N':
        break
media = soma/len(pessoas)
print(pessoas)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'B) A média das idades é de {media:5.2f} anos')
print(f'C) A(s) mulhere(s) cadastrada(s) é/são: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
        print()
print(f'A lista de pessoas com idade acima da média é: ', end='')
for p in pessoas:
    if p['idade'] >= media:
        print(' ')
        for k,v in p.items():
            print(f'{k} = {v}', end='')
            print()
print('<<<< ENCERRADO >>>>')
