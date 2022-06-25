larg = float(input("Qual a largura da parede que quer pintar?(Digite o valor em metros) "))
alt = float(input("E qual a altura dessa parede? "))

area = larg * alt

litro = area/2

print('A área dessa parede é de {} metros quadrados e a quantidade de litros para pintá-la é de {}L'.format(area, litro))