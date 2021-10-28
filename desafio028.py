import random

n = random.randint(1,5)
nuser = int(input('Digite um número inteiro de 1 a 5: '))

if n == nuser:
    'Acertou Mizeravi'
    print('O valor de n={} é igual a nuser={}; Você Venceu.'.format(n,nuser))
else:
    'Falhou Hardcoremente'
    print('O valor de n={} é diferente de nuser={}; Você perdeu.'.format(n,nuser))
