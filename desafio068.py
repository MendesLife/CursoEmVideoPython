#Escolher se quer para ou impar
#jogar um número
#Somar e ver se o resultado é par ou impar

import random

while True:
    soma = 0
    meu = input('Escolha entre PAR ou IMPAR: ').strip().upper()
    pc = ''
    if meu == 'PAR':
        pc=='IMPAR'
        meun=int(input('Escolha um número entre 0 a 9: '))
        pcn = random.randint(0,9)

        soma = meun + pcn

        print(f'Você escolheu o número {meun} e o pc escolheu o número {pcn} a soma foi {soma}')

        if soma %2 == 0:
            print('Você ganhou')
        else:
            print('PC ganhou')
            break

    else:
        pc =='PAR'
        meu =='IMPAR'
        meun=int(input('Escolha um número entre 0 a 9: '))
        pcn = random.randint(0,9)
        soma = meun + pcn

        soma = meun + pcn

        print(f'Você escolheu o número {meun} e o pc escolheu o número {pcn} a soma foi {soma}')

        if soma %2 == 0:
            print('PC ganhou')
            break
        else:
            print('Você ganhou')
            
print('FIM DO JOGO')


    