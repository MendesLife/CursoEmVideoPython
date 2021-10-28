import random

n1=random.randint(1,9)
n2=random.randint(1,9)
n3=random.randint(1,9)

print('{},{},{}'.format(n1,n2,n3))

if n1<(n2+n3) and n2<(n1+n3) and n3<(n1+n2):
    print('Pode ser um triângulo')
else:
    print('Não pode ser um triângulo.')
    