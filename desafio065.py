resposta = 'S'
soma = x = maior = menor = 0

while resposta =='S':
    n = float(input('Digite um número: '))
    soma = soma +  n
    if x == 0:
        maior = n
        menor = n
    if n>maior:
        maior = n
    if n<menor:
        menor = n
    x+=1
    resposta = str(input('Deseja Continuar S/N: ')).strip().upper()
print('Fim')
media = soma / x
print('A média vale {:.2f}.'.format(media))
print('o maior valor é {} e o menor valor é {}.'.format(maior,menor))