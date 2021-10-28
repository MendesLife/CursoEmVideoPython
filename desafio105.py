def notas(*n,sit=False):
    ficha = {}
    ficha['total'] = len(n)
    ficha['maior'] = max(n)
    ficha['menor'] = min(n)
    ficha['media'] = sum(n)/len(n)
    if sit:
        if ficha['media'] >=7:
            ficha['situação'] = 'BOA'
        if ficha['media'] >=5:
            ficha['situação'] = 'RAZOÁVEL'
        else:
            ficha['situação'] = 'RUIM'

    return ficha


resp = notas(5.5,2.5,8.5)
print(resp)