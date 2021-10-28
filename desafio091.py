import random
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': random.randint(1,6),
             'jogador2': random.randint(1,6),
             'jogador3': random.randint(1,6),
             'jogador4': random.randint(1,6)}
print('Valores sortedaos:')
# for k, v in jogadores.items():
#     print(f'O {k} tirou o valor {v}.')
#     sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)