#Fatiamento de String
nfrase = '  Aprenda Python  '
frase ='Curso em Vídeo Python'
print(frase[9])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise

print(len(frase))
print(len(nfrase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print('Curso'in frase)

#Transformação

print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(nfrase.strip())
print(nfrase.rstrip())
print(nfrase.lstrip())

#divisão

print(frase.split())

#junção

print('-'.join(frase))
