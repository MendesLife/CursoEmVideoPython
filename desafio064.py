n = int(input('Digite um valor: '))
x=0
soma = 0

while n != 999:
    soma +=n
    x= x+1
    n = int(input('Digite um valor: '))
print('Foram digitados {} números e a soma deles é {}'.format(x,soma))