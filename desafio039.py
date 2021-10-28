import random as rd


ano = rd.randint(2000, 2008)
data = 2021
idade = data - ano

print('Você tem {}.'.format(idade))

if idade < 18:
    print('Ainda faltam {} anos pra você se alistar.'.format(18-idade))
elif idade == 18:
    print('Chegou a hora de se alistar.')
elif idade > 18:
    print('Pasou o ano do seu alistamento já vai fazer {} anos.'.format(idade-18))
