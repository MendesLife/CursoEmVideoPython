import random

ano= random.randint(1997, 2015)
idade = 2021 - ano

print('Sua idade é de {} anos.'.format(idade))

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <=19:
    print('Junior')
elif idade <=20:
    print('Sênior')
elif idade > 20:
    print('Master')
