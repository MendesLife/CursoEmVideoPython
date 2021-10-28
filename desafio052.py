n=int(input('Digite um valor inteiro: '))
contador=0

for c in range(1,n):
    if n%c == 0:
        contador+=1
if contador == 1:
    print('Número primo')
else:
    print('Não é primo')
