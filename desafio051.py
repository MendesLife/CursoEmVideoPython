n= int(input('Digite o priemiro termo: '))
razao = int(input('Digite a razão: '))
decimo = n + (10)*razao

for c in range(n,decimo,razao):
    print('{}'.format(c), end=' → ')
print('Acabou')