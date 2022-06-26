# Desafio 044
from time import sleep
valor = float(input('Digite o valor a ser pago: R$'))
print('Escolha a forma de pagamento')
print('[1] à vista dinheiro/cheque (10% de desconto)')
print('[2] à vista no cartão (5% de desconto')
print('[3] em até 2x no cartão (preço formal)')
print('[4] 3x ou mais (5% de juros)')
opcao = int(input('Digite o número da opção selecionada: '))

print('CALCULANDO...')
sleep(3)

if opcao == 1:
    novoVal = valor - (valor * (10/100))
    print('Opção selecionada: {}'.format(opcao))
    print('O valor original de R${:.2f} fica agora R${:.2f}'.format(valor, novoVal))
elif opcao == 2:
    novoVal = valor - (valor * (5 / 100))
    print('Opção selecionada: {}'.format(opcao))
    print('O valor original de R${:.2f} fica agora R${:.2f}'.format(valor, novoVal))
elif opcao == 3:
    print('Opcação selecionada: {}'.format(opcao))
    print('O valor permanece R${:.2f}'.format(valor))
elif opcao == 4:
    print('Opcação selecionada: {}'.format(opcao))
    parcela = int(input('Deseja parcelar em quantas vezes? '))
    novoVal = valor * 1.2
    parcelaValor = novoVal / parcela
    print('Você escolheu parcelar em {}x'.format(parcela))
    print('CALCULANDO...')
    sleep(3)
    print('O valor original de R${:.2f} fica agora R${:.2f} em {} parcelas de R${:.2f}'.format(valor, novoVal, parcela, parcelaValor))
else:
    print('[ERRO] Opção inválida! Tente novamente')


