import random

numeros = []
pares = []


def programa():

    def sorteia():
        for i in range (5):
            numeros.append(random.randint(1,100))
        print(numeros)
    sorteia()
    def somaPar():
        soma = 0
        for c in numeros:
            if c%2 == 0:
                soma+=c
                pares.append(c)
        print(f'A soma entre os números {pares} foi {soma}.')
    somaPar()



programa()
