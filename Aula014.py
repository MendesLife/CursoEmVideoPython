# while not maça :
#     print('passo')
# print('pega')

# while not maça:
#     if chao == 'True':
#         print('passo')
#     if buraco == 'True':
#         print('pule')
#     if moeda == 'True':
#         print('pega')
# print('pega')

# for c in range(1,10):
#     n = int(input('Digite um valor: '))
# print('FIM')

# n = 1
# r = 'S'

# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar [S/N]: ')).upper()
# print('FIM')

n = 1 

par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('A quantidade de números pares é {} e de números impares é {}'.format(par, impar))

