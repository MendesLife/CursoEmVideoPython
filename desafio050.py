import random

soma=0

for n in range(0,6):
    a=random.randint(1,9)
    print(a)
    if a%2 == 0:
        soma+=a
   
print('O resultado da soma dos números pares é {}.'.format(soma))