import random

lista = [[],[]]
valor= 0
for c in range (1,8):
    valor = random.randint(1,100)
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
# print(f'Os valores são: {lista}.')
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são {lista[0]}.')
print(f'Os valores impares são {lista[1]}.')