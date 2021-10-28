def aumentar(n,porcentagemAumento,formatado=False):
    if formatado == 'S':
        return moeda(n+((n*porcentagemAumento)/100))
    else:
        return(n+((n*porcentagemAumento)/100))

def diminuir(n,porcentagemReduz,formatado=False):
    if formatado == 'S':
        return moeda(n-((n*porcentagemReduz)/100))
    else:
        return(n-((n*porcentagemReduz)/100))

def dobro(n,formatado=False):
    if formatado == 'S':
        return moeda(n*2)
    else:
        return(n*2)

def metade(n,formatado=False):
    if formatado == 'S':
        return moeda(n/2)
    else:
        return(n/2)

def moeda(n):
    return(f'R${n:.2f}')

def resumo(n,porcentagemAumento,porcentagemReduz):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado:    {moeda(n)}')
    print(f'Dobro do preço:     {moeda(dobro(n))}')
    print(f'Metade do preço:    {moeda(metade(n))}')
    print(f'{porcentagemAumento}% de aumento:     {moeda(aumentar(n,porcentagemAumento))}')
    print(f'{porcentagemReduz}% de redução:     {moeda(diminuir(n,porcentagemReduz))}')