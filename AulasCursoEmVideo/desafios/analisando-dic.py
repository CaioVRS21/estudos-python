def notas (*n, sit = False):
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] > 7:
            r['Situação'] = 'BOA'
        elif 5 < r['Média'] < 7:
            r['Situação'] = 'RAZOAVÉL'
        else:
            r['Situação'] = 'RUIM'
    return r
resp = notas(5.5, 2.5, 9, 8.5, sit=True)
print(resp)