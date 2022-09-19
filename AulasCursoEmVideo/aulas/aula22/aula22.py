#Aula 22 sobre modularização
#O foco da modularização é dividir um programa em "pedaços menores", ou seja dividir ele em diversas funções cada uma com seu propósito deixando ele mais legível
import uteis

num = int(input('Digite um número: '))
f = uteis.fatorial(num)
dbr = uteis.dobro(num)
trip = uteis.triplo(num)
print(f)
print(f'O dobro de {num} é {dbr}')
print((f'O triplo de {num} é {trip}'))