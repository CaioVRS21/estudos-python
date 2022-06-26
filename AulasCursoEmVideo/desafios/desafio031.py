print('Bem-vindo a nossa calculadora de valores!')
print('Informamos que nossas tarifas são: R$0.50 por km para viagens de até 200km e R$0.45 por km para viagens mais longas')
distancia = float(input('Digite em km a distância da sua viagem: '))

if distancia > 200:
    valor = distancia * 0.45
    print('Sua viagem é de {:.1f}km logo seu custo é de R${:.2f} reais'.format(distancia, valor))
else:
    valor = distancia * 0.50
    print('Sua viagem é de {:.1f}km logo seu custo é de R${:.2f} reais'.format(distancia, valor))