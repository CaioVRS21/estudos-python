#Desafio 036
print('Bom-dia e bem-vindo(a) ao Veras Bank!')
print('Vamos ver se você pode ter um empréstimo liberado')
valor = float(input('Qual o valor da propriedade que você deseja comprar? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
ano = int(input('Você pretende pagar em quantos anos? '))

mes = ano*12
prest = valor/mes
porcentSal = salario * (30/100)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, ano, prest))
if prest >= porcentSal:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo LIBERADO!')
