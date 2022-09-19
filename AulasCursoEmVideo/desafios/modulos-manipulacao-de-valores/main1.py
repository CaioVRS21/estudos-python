import funcoes1
val = float(input('Digite um valor: R$'))
mtd = funcoes1.metade(val)
dbr = funcoes1.dobro(val)
amntd = funcoes1.aumento(val)
print(f'A metade de R${val} é R${mtd}')
print(f'O dobro de R${val} é R${dbr}')
print(f'Aumentando R${val} em 10% ficamos com R${amntd}')