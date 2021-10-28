import random

media = 0
nomevelho = ''
maioridade = 0
mmvinte = 0

for c in range(0,4):
    nome=input('Digite seu nome: ')
    idade=random.randint(1,80)
    sexo=str(input('Digite seu sexo: ')).strip().upper()
    media += idade
    if sexo =='M' and idade> maioridade:
        maioridade=idade
        nomevelho=nome
    elif sexo =='F' and idade<20:
        mmvinte += 1
        


media = media/4
print('A média de idade é {} anos.'.format(media))
print('{} é o homem mais velho e tem {} anos.'.format(nomevelho,maioridade))
print('A quantidade de mulheres maiores que 20 anos é {}.'.format(mmvinte))


