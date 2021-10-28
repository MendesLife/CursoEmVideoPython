cidade = str(input('Digite em que cidade você nasceu: ')).strip().upper()

print('Você nasceu em {}'.format(cidade))

padrao = 'SANTO'

desvincula = cidade.split()

resposta = desvincula[0]

if resposta == padrao:
    print('Bem-Vindo de volta irmão.')
else:
    print('Lugar errado parceiro.')

