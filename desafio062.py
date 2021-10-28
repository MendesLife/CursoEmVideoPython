n= int(input('Digite o priemiro termo: '))
razao = int(input('Digite a razão: '))
termo = n
contador =1
total = 0
mais = 10

while mais !=0:
    total = total + mais
    while contador<=total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        contador = contador+1
    print('PAUSA')
    mais=int(input('Você quer mostrar mais algum termo ?'))
print('FIM')