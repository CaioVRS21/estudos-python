from math import sin, cos, tan, radians
angulo = float(input('Digite o valor de um ângulo para saber seu seno, cosseno e tangente: '))
radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print("O angulo digitado foi {}, seu seno é {}, cosseno {} e sua tangente é de {}".format(angulo, seno, cosseno, tangente))