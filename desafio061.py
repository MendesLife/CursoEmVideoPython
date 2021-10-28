n= int(input('Digite o priemiro termo: '))
razao = int(input('Digite a razão: '))
termo = n
contador =1

while contador<=10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    contador = contador+1
print('fim')