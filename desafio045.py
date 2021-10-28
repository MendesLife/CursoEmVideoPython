import random

meu= str(input('Escolha entre pedra,papel ou tesoura: ')).strip().upper()
pc = random.choice(['PEDRA','PAPEL','TESOURA'])

print('Você escolheu {} e o pc escolheu {}.'.format(meu,pc))

if meu == 'PEDRA' and pc == 'PAPEL' or meu =='PAPEL' and pc == 'TESOURA' or meu == 'TESOURA' and pc == 'PEDRA':
    print('\033[31mVencedor PC.\033[m')
elif meu == pc:
    print('\033[33mEmpate.\033[m')
else:
    print('\033[32mVencedor VOCÊ.\033[m')