import random

n = random.randint(0,10)
nuser = int(input('Digite um número inteiro de 0 a 10: '))

while nuser!=n:
    nuser = int(input('Valor errado, tente novamente digitando outro valor de 0 a 10: '))
print('Muito bem você acertou o valor do computador era {}.'.format(n))