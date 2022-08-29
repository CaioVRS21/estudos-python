lanche = ['hamburger', 'refrigerante', 'pizza', 'picolé']
lanche.append('suco') #para adicionar um elemento ao final de uma lista
lanche.insert(2, 'água') #com insert é necessário colocar o index aonde o novo elemento será adicionado, neste caso 'água entra no index 3 e empurra os demais adiante sem substituir o antigo valor do index 2
del(lanche[2]) #para deletar uma lista ou neste caso, um valor especifico dentro da lista
#lanche.pop(2)
#lanche.remove('picolé')
#ambos os métodos acia são para remover itens, o pop caso não seja declarado o index a ser retirado irá retirar sempre o último elemento, enquanto remove() apaga um valor especifico
if 'refrigerante in pizza': #para checar se há um valor dentro de um lista, caso esse valor exista o bloco de código será efetuado
    lanche.remove('refrigerante')
valores = list(range(4, 11)) #list() cria uma lista vazia há ser preenchida ou que se complete com meios como o range, neste exemplo uma lista de 4 a 10 (o último elemento do range (11 neste caso) é sempre eliminado/descontado
valores2 = [8, 3, 7, 4, 1, 9, 10, 2, 5, 6]
valores2.sort() #sort deixa os valores de uma lista em ordem crescente
valores2.sort(reverse=True) #com o "reverse = True" os valores são ordenados de forma decrescente
#len(valores) retorna o tamanho da lista

num = [2, 4, 7, 8, 4, 1, 4]
while 4 in num:
    num.remove(4)
valores3 = list()
valores3.append(5)
valores3.append(9)
valores3.append(4)
#for c, v in enumerate(valores3):
    #print(f'Na posição {c} eu encontrei o valor {v}!')
#print('Cheguei no final da lista')

a = [2, 3, 4, 7]
b = a #deste modo b não é uma cópia de a mas sim as duas são a mesma lista, logo alterando qualquer valor em b também altera em a como no exemplo abaixo
b[2] = 8
print(a)
print(b)
#para que seja feita um cópia dde fato faz-se o seguinte:
c = [2, 3, 4, 7]
d = c[:]
d[2] = 8
print(c)
print(d)