def fatorial(n,show='n'):
    f = 1
    for c in range(n,0,-1):
        f*=c
        if show in 'S' and c !=1: 
            print(f'{c} x',end=' ')
        else:
            print(f'{c} ',end='')
            
    print(f'= {f}')


fatorial(int(input('Digite um valor a ser fatorado: ')),show=str(input('Deseja mostrar o valor na tela[S/N]: ')).strip().upper())

