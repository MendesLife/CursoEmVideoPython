import math

op = float(input('Digite o valor do cateto oposto: '))
ad = float(input('Digite o valor do cateto adjacente: '))

hipo = math.sqrt(op** 2 + ad ** 2)

print('A hipotenusa vai medir {:.2f}'.format(hipo))