# Desafio 53
frase = input('Digite algo: ').strip().upper()
palavras = frase.split()
tudoJunto = ''.join(palavras)
invertido = ''
for letra in range(len(tudoJunto) -1, -1, -1):
    invertido += tudoJunto[letra]
print('Você digitou {} que invertido fica {}'.format(tudoJunto, invertido))
if invertido == tudoJunto:
    print('É palíndromo!')
else:
    print('Não é um palíndromo')
