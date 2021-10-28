import random
lista = []
listapar = []
listaimpar = []
while True:
    lista.append(random.randint(1,100))
    resp=str(input('Deseja continuar [S/N]'))

    if resp in 'Nn':
        break
for i,v in enumerate(lista):
    if v%2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)

listapar.sort()
listaimpar.sort()
print(f'A lista completa é {lista}.')
print(f'A lista par é composta pelos números {listapar}.')
print(f'A lista impar é composta pelos números {listaimpar}.')
