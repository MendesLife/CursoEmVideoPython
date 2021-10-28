import random

n1=random.randint(1,9)
n2=random.randint(1,9)
n3=random.randint(1,9)

print('O valor de n1={},n2={} e n3={}'.format(n1,n2,n3))

if n1==n2 and n2==n3:
    print('Se trata de um triângulo equilátero.')
elif n1==n2 or n1==n3 or n2 == n3:
    print('Se trata de um triângulo isósceles.')
elif n1!=n2 and n1!=n3 or n2 != n3:
    print('Se trata de um triângulo escaleno.')