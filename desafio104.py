def leiaInt():
    while True:
        n=input('Digite um n°: ')
        if n.isnumeric():
            print(f'Você acabou de digitar o número {n}.')
            break
        else:
            print('Valor digitado errado.')
            

leiaInt()