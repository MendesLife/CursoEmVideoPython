import random as rd
import math

n = rd.randint(1,100)

print('O número é {}.'.format(n))

xoic = input('Qual será a base de conversão BINÁRIO,OCTAL,HEXADECIMAL: ').strip().upper()

if xoic == 'BINÁRIO':
    print('O valor de {} em BINÁRIO é {}'.format(n,bin(n) ))
elif xoic == 'OCTAL':
    print('O valor de {} em OCTAL é {}'.format(n,oct(n) ))
elif xoic == 'HEXADECIMAL':
    print('O valor de {} em HEXADECIMAL é {}'.format(n,hex(n) ))