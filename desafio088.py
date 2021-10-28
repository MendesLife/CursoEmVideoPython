import random
from time import sleep
lista = []
jogos = []
print('JOGO DA MEGA SENA')
quant = int(input('Quantos jogos seram sorteados: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print(f'Sorteando {quant} jogos.')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
