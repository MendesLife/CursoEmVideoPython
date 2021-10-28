n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

numeros = (n1,n2,n3,n4)

print(f'O valor 9 apareceu {numeros.count(9)} vez.')
print(f'O número 3 apareceu na posição {numeros.index(3)+1}.')

pares=[]

for n in range(len(numeros)):   
    if numeros[n]%2 == 0:
        pares.append(numeros[n])
    
    
print(f'Os números pares foram {pares}.')