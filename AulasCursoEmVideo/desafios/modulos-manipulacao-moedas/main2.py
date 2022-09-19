import funcoes2
val = float(input('Digite um valor: R$'))
mtd = funcoes2.metade(val)
dbr = funcoes2.dobro(val)
taxa = 10
amntd = funcoes2.aumento(val, taxa)
dmnd = funcoes2.diminuir(val, taxa)
print(f'A metade de {funcoes2.moeda(val)} é {funcoes2.moeda(mtd)}')
print(f'O dobro de {funcoes2.moeda(val)} é {funcoes2.moeda(dbr)}')
print(f'Aumentando {funcoes2.moeda(val)} em {taxa}% ficamos com {funcoes2.moeda(amntd)}')
print(f'Diminuindo {funcoes2.moeda(val)} em {taxa}% ficamos com {funcoes2.moeda(dmnd)}')