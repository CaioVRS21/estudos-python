import funcoes3
val = float(input('Digite um valor: R$'))
mtd = funcoes3.metade(val)
dbr = funcoes3.dobro(val)
taxa = 10
amntd = funcoes3.aumento(val, taxa)
dmnd = funcoes3.diminuir(val, taxa)
print(f'A metade de {funcoes3.moeda(val)} é {funcoes3.moeda(mtd, True)}')
print(f'O dobro de {funcoes3.moeda(val)} é {funcoes3.moeda(dbr, True)}')
print(f'Aumentando {funcoes3.moeda(val)} em {taxa}% ficamos com {funcoes3.moeda(amntd, True)}')
print(f'Diminuindo {funcoes3.moeda(val)} em {taxa}% ficamos com {funcoes3.moeda(dmnd, True)}')