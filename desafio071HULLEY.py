nota01 = 0
nota10 = 0
nota20 = 0
nota50 = 0

valor = int(input('Valor:'))

if (valor/50 >= 1):
    nota50 = int(valor/50)
    valor = valor%50

if (valor/20 >= 1):
    nota20 = int(valor/20)
    valor = valor%20
    
if (valor/10 >= 1):
    nota10 = int(valor/10)
    valor = valor%10

if (valor/1 >= 1):
    nota01 = int(valor/1)
    valor = valor%1

print('Cédulas de 50 - ' + str(nota50))
print('Cédulas de 20 - ' + str(nota20))
print('Cédulas de 10 - ' + str(nota10))
print('Cédulas de 01 - ' + str(nota01))
