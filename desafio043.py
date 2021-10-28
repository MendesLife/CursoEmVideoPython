altura= float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

IMC = peso/(altura*altura)


if IMC < 18.5:
    print('Abaixo do peso.')
if IMC >= 18.5 and IMC<25:
    print('Ideal.')
if IMC >= 25 and IMC<30:
    print('Sobrepeso.')
if IMC >= 30 and IMC<40:
    print('Obesidade.')
if IMC > 40:
    print('Obesidade Mórbida.')
print('Seu IMC vale {}.'.format(IMC))