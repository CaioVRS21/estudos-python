dias = int(input("Quantos dias você utilizou o carro? "))
km = float(input("Você rodou por quantos Km com o carro? "))


result = (dias * 60) + (km * 0.15)

print('O total a pagar é R${:.2f}'.format(result))
