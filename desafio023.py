n=int(input('Digite um número de 0 a 9999: '))
n = str(n)

print('O número digitado foi {}'.format(n))
print('O mihar vale {}'.format(n[:1]))
print('O centena vale {}'.format(n[1:2]))
print('O dezena vale {}'.format(n[2:3]))
print('O unidade vale {}'.format(n[3:4]))

n = int(n)