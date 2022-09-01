dados = []
media = 0
while True:
    nomes = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    dados.append([nomes, [n1, n2], media])
    decisao = str(input('Deseja continuar?[S/N] '))
    if decisao in 'Nn':
        break;
print('-='*30)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(dados):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    ('-'*26)
    decisao2 = int(input('Deseja ver as notas de qual aluno?(999 Interrompe) '))
    if decisao2 == 999:
        print('FINALIZANDO...')
        break;
    if decisao2 <= len(dados) - 1:
        print(f'Notas de {dados[decisao2][0]} são {dados[decisao2][1]}')
print('<<< VOLTE SEMPRE >>>')