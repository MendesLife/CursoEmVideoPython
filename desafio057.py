sexo= str(input('Informe se seu sexo é [M/F]: ')).strip().upper() [0]

while sexo not in 'MmFf':
    sexo = str(input('Digite um sexo válido: ')).upper().strip()[0]
print('Seu sexo é {}.'.format(sexo))