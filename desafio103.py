def ficha(nome='',gols=0):
    nome = str(input('Nome do Jogador: '))
    gols = str(input('Quantidade de gols marcados: '))
    if nome == '':
        nome = 'Desconhecido'
    if gols == '':
        gols = 0
    print(f'O jogador {nome} marcou {gols} gol(s) no campeonato.')


ficha()




