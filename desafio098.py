def contador(inicio,fim,passo):
    print('-'*30)
    if passo >= 0:
        fim+=1
    else:
        fim-=1
    if passo == 0:
        passo=1

    for i in range(inicio,fim,passo):
        print(i,end=' ')
    print('Fim!')
    print('-'*30)

contador(1,10,1)
contador(10,0,-2)
contador(inicio=int(input('Inicio: ')),fim=int(input('Fim: ')),passo=int(input('Passo: ')))


