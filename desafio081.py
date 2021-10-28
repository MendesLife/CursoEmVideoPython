lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(f'A quantidade de itens digitados foi {len(lista)}.')
lista.sort(reverse=True)
print(f'Os valores da lista são {lista}.')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')