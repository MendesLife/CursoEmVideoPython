nome = str(input('Digite seu nome: ')).strip()

print(nome.upper())
print(nome.lower())
print(len(nome)- nome.count(' '))
print(nome.find(' '))

separa = nome.split()
print(separa)
print(len(separa[0]))
