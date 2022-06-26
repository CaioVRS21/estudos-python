km = int(input('Em km/h diga o quão rápido o veículo estava indo: '))
limite = 80
if km > 80:
    multa = (km - limite) * 7
    print('Você ultrapassou o limite de velocidade! Você estava a {}km/h, sua multa é de R${:.2f}'.format(km, multa))
else:
    print('Ai sim! O veículo estava a {}km/h e respeitando o limite de velocidade!'.format(km))