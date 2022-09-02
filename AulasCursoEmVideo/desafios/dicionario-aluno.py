aluno = {}
aluno['nome'] = str(input('Digite um nome: '))
aluno['média'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['média'] >=7 :
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5 and aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} do aluno é {v}')

