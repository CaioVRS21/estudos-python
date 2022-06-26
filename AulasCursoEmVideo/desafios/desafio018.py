from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um ângulo para saber seu seno, cosseno e tangente: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print("O angulo digitado foi {:.2f}, seu seno é {:.2f}, cosseno {:.2f} e sua tangente é de {:.2f}".format(angulo, seno, cosseno, tangente))