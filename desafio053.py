frase = str(input('Digite uma frase: ')).strip().upper()

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('É um palindromo')
else:
    print('Não é um palindromo')
