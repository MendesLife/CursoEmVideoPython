import random

peso = 0
leve = 0
pesado = 0

for c in range(0,5):
    n=random.randint(60,90)
    print(n)
    if c == 0:
        pesado = n
        leve = n
    if n>pesado:
        pesado=n
    elif n<leve:
        leve=n
print('O mais leve pesa {}kg.'.format(leve))
print('O mais pesado pesa {}kg.'.format(pesado))