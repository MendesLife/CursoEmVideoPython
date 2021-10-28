from math import dist
import random

distancia =  random.randint(100,300)

valor = 0

if distancia > 200:
    valor = distancia*0.45
    print('Você andou {}Km e o valor total é {}.'.format(distancia,valor))
else:
    valor = distancia*0.50
    print('Você andou {}Km e o valor total é {}.'.format(distancia,valor))