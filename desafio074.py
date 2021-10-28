import random

numero1 = random.randint(0,100)
numero2 = random.randint(0,100)
numero3 = random.randint(0,100)
numero4 = random.randint(0,100)
numero5 = random.randint(0,100)

numeros = (numero1,numero2,numero3,numero4,numero5)

print(f'Os números são {numeros}.')

for n in range (len(numeros)):
    if n == 0:
        numeromaior = numeros[n]
        numeromenor = numeros[n]
    if numeros[n] > numeromaior:
        numeromaior = numeros[n]
    elif numeros[n] < numeromenor:
        numeromenor = numeros[n]
print(f'O número maior vale {numeromaior} e o número menor vale {numeromenor}.')


