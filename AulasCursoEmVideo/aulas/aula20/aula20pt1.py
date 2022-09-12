def falaOi ():
    print('Oi')
    return ''
def soma(x, y):
    soma = x + y
    print(soma)
    return soma
def mensagem(msg):
    print("-"*30)
    print(msg)
    print('-'*30)
    return True
def desempacota (* num): #o "*" simboliza para o python que multiplos parametros serão recebidos pela variavel e esta vira uma tupla contendo os valores passados, isto não é necessário se o parâmetro que deseja ser passado for uma lista/array
    print(num)
desempacota(1, 5, 2, 5)
desempacota(5, 7, 2)
desempacota(3)