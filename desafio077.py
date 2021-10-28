palavras = ('batata','lpl','soul')


for p in palavras:
    print(f'\nNA palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou': 
            print(letra,end='')
    