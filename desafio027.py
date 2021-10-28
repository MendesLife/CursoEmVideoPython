nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome é: {}.'.format(nome))

print('Seu primeiro nome é: {}.'.format(nome.split()[0]))
print('Seu último nome é: {}.'.format(nome.split()[len(nome.split())-1]))