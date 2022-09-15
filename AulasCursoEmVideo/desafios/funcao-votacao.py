from datetime import date
def votacao (anoNasc):
    anoAt = date.today().year
    idade = anoAt - anoNasc
    if 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade < 16:
        return f'Com {idade} anos: NÂO VOTA'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
anoNasc = int(input('Em que ano você nasceu? '))
print(votacao(anoNasc))