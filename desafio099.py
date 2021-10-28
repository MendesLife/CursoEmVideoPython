def maior(*num):
    numeros=[]
    for i in num:
        numeros.append(i)
    numeros.sort(reverse=True)
    print('-'*(len(numeros)+2))
    print(f' O maior número é {numeros[0]}.')
    print('-'*(len(numeros)+2))
    



maior(2,10,30,5,8,23,14,58)
maior(2,10,70,5,8,23,14,58)