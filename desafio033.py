import random

n1 = random.randint(1,9)
n2 = random.randint(1,9)
n3 = random.randint(1,9)

lista = [n1,n2,n3]

print('Os 3 números são {}'.format(lista))

maior_numero = 0
menor_numero = 9

for numero in lista:
    if numero > maior_numero:
        maior_numero=numero
    if numero < menor_numero:
        menor_numero=numero

print('O maior número vale {}.'.format(maior_numero))
print('O menor número vale {}.'.format(menor_numero))
