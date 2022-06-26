print('Vamos saber o aumento do seu salário')
sal = float(input('Digite o valor do seu salário: R$'))

if sal > 1250.00:
    aumento = sal * 1.1
    print('O seu salário antes era de R${:.2f}, agora com o aumento de 10% ele fica em R${:.2f}'.format(sal, aumento))
else:
    aumento = sal * 1.15
    print('O seu salário antes era de R${:.2f}, agora com o aumento de 10% ele fica em R${:.2f}'.format(sal, aumento))