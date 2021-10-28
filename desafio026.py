frase = str(input('Digite uma frase: ')).strip().lower()

print('A frase {} tem {} letras. '.format(frase, len(frase)))
print('A letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A letra "A" aparece pela primeira vez na {} casa. '.format(frase.find('a')+1))
print('A letra "A" aparece pela última vez na {} casa. '.format(frase.rfind('a')+1))

#Andando descalço por ai.