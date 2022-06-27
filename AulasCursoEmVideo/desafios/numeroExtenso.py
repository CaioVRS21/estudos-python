#Desafio 072
numExt = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numVal = int(input('Digite um número inteiro entre 0 e 20: '))
    if numVal < 0 or numVal > 20:
        print('[ERRO] Valor inválido tente novamente')
    else:
        print(numExt[numVal])
        break
