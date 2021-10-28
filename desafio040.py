import random

nome = str(input('Digite seu nome:'))
n1= float(input('Digite o valor da primeira nota: '))
n2= float(input('Digite o valor da desgunda nota: '))
media = (n1+n2)/2

print('Sua primeira nota foi {}, sua segunda nota foi {}, sua média foi {}.'.format(n1,n2,media))

if media < 5:
    print('Que pena {}, você foi Reprovado.'.format(nome))
elif media >= 5 and  media <7:
    print('{} você tera que estudar mais porque está de Recuperação.'.format(nome))
elif media >= 7: 
    print('Parbéns {} você foi Aprovado.'.format(nome))
