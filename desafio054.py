import random

ano_atual=2021



for c in range(0,7):
    n=random.randint(1997,2010)
    idade = ano_atual-n
    if idade >= 18:
        print('Você tem {}anos,Maior de idade'.format(idade))
    else: 
        print(('Você tem {}anos,Menor de idade'.format(idade)))