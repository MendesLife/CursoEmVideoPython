import random

n= random.randint(0,9)

if n%2 == 0:
    print('O número {} é par.'.format(n))
else: 
    print('O número {} impar.'.format(n))