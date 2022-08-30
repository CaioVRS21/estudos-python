#Aula sobre listas compostas
#index principal: 0             1              2
pessoas = [['Caio', 21], ['Melo', 22], ['Bruno', 23]]
#secundario: 0       1      0      1      0       1
print(pessoas[0][0]) #print o primeiro valor dentro da primeira lista
print(pessoas[1][0]) #print o primeiro valor dentro da segunda lista
print(pessoas[2]) #print a terceira lista completa
#É possível adicionar uma lista dentro da outra pelo método append
galera = list()
galera.append(pessoas)
print(galera)