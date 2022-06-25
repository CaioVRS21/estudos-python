from datetime import date

dia = input('Em que dia você nasceu? ')
mes = input('Em que mês você nasceu? ')
ano = input('Em que nao você nasceu? ')
anoAtual = date.today().year
idade = anoAtual - int(ano)

print('Se você nasceu em:', dia, '/', mes, '/', ano, 'Você tem', idade, 'anos')
