nome = str(input('Digite o seu nome completo: ')).strip().upper()

padrao = 'SILVA'

checador = (padrao in nome)

if checador == True:
    print('Era só mais um Silva.')
else:
    print('Tu é playboy mermão.')

