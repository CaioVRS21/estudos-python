#Desafio 040
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media < 5.0:
    print('Sua média é de {:.1f}, você está REPROVADO!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é de {:.1f}, você está EM RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é de {:.1f}, você está APROVADO!'.format(media))