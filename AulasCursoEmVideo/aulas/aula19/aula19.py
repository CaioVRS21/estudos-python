#Dicionários
pessoa = {"nome": 'Caio', "idade": 21}
pessoa['sexo'] = 'M' #cria um novo elemento
del(pessoa['idade']) #para deletar uma chave e seu valor
filme = {'título': 'Star Wars', 'lançamento': 1977, 'diretor': 'George Lucas'}
#print(filme.values()) #retorna um array com apenas os valores de um dicionário
#print(filme.keys()) #retorna um array com apenas as chaves/índices de um dicionário
#print(filme.items()) #retorna as chaves e seus respectvos valores dentro de um tupla que está dentro de um array
#for k, v in filme.items(): #função similar ao enumerate()
#print(f'O {k} é {v}')
locadora = [{'título': 'Star Wars', 'lançamento': 1977, 'diretor': 'George Lucas'}, {'título': 'Avengers', 'lançamento': 2012, 'diretor': 'Jass Whedon'}, {'título': 'Matrix', 'lançamento': 1999, 'diretor': 'Wachowski'}]
#print(locadora[0]['lançamento'])
brasil = []
estado1 = {'uf': 'Amazonas', 'sigla': 'AM'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#brasil.append(estado1)
#brasil.append(estado2)
#como demonstrado anteriormente, uma lista composta pode comportar dicionários dentro de si
#print(brasil)
#No python para que multiplos dados sejam inseridos em um dicionário a melhor solução seria usar o fatiamento como forma de criar um cópia do dicionário até o fim do laço, porém em um dicionário não épossível realizar o fatiamento, o método correto é .copy(), como no exemplo abaixo
estado = {}
for c in range(0, 3):
    estado['uf'] = str(input('Digite o nome da Unidade Federativa: '))
    estado['sigla'] = str(input('Digite a sigla desta UF: '))
    brasil.append(estado.copy())
print(brasil)