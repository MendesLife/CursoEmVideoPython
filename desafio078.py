import random

listanum = []
for c in range (0,5):
    listanum.append(random.randint(1,100))
    if c == 0:
        menorvalor = maiorvalor = listanum[c]
    else: 
        if listanum[c] > maiorvalor:
            maiorvalor = listanum[c]
        if listanum[c] < menorvalor:
            menorvalor = listanum[c]
        
print(f'Os valores da lista são {listanum}')
print(f'O maior valor digitado foi {maiorvalor} nas posições')
for i,v in enumerate(listanum):
    if v == maiorvalor:
        print(f'{i+1}...', end='')
print()
print(f'O menor valor digitado foi {menorvalor} nas posições')
for i,v in enumerate(listanum):
    if v == menorvalor:
        print(f'{i+1}...', end='')
print()