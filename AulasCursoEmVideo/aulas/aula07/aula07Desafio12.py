valor = float(input('Digite um valor para receber um desconto de 5%: R$'))

result = valor - (valor * 5/100)

print('O valor era de R${:.0f} e após o desconto ele ficou R${}'.format(valor, result))