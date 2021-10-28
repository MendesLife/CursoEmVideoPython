import random as rd

n1 = rd.randint(1,9)
n2 = rd.randint(1,9)

print('Os valores de n1={} e n2={}.'.format(n1, n2))

if n1 > n2:
    print('O primeiro valor é maior que o segundo.')
elif n2 > n1:
    print('O segundo valor é maior que o primeiro.')
else:
    print('Não existe valor maior, os dois são iguais.')