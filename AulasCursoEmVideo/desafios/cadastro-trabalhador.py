from datetime import datetime
pessoa = {}
pessoa['Nome'] = str(input('Digite o nome do trabalhador: '))
pessoa['Idade'] = datetime.now().year - int(input('Digite o ano de nascimento desta pessoa: '))
pessoa['Carteira de Trabalho'] = int(input('Digite o número da Carteira de Trabalho desta pessoa:(Digite 0 caso esta não tenha) '))
if pessoa['Carteira de Trabalho'] == 0:
    for k,v in pessoa.items():
        print(f'{k} tem o valor {v}')
else:
    pessoa['Contratação'] = int(input('Em que ano esta pessoa foi contratada? '))
    pessoa['Salário'] = float(input('Qual o valor do salário desta pessoa? R$'))
    pessoa['aposentadoria'] = ((pessoa['Contratação'] + 35) - datetime.now().year) + pessoa['Idade']
    for k,v in pessoa.items():
        print(f'- {k} tem o valor {v}')
