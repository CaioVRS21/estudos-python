import funcoes1
val = float(input('Digite um valor: R$'))
mtd = funcoes1.metade(val)
dbr = funcoes1.dobro(val)
taxa = 10
amntd = funcoes1.aumento(val, taxa)
dmnd = funcoes1.diminuir(val, taxa)
print(f'A metade de R${val} é R${mtd}')
print(f'O dobro de R${val} é R${dbr}')
print(f'Aumentando R${val} em {taxa}% ficamos com R${amntd}')
print(f'Diminuindo R${val} em {taxa}% ficamos com R${dmnd}')