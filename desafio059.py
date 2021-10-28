n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números  
    [5]sair do programa''')
    opcao = int(input(' >>>>> Qual é a sua opção: '))
    if opcao == 1:
        resultado = n1+n2
        print('O resultado da soma entre {} e {} é {}.'.format(n1,n2,resultado))
    elif opcao == 2:
        resultado = n1*n2
        print('O resultado da multiplicação entre {} e {} é {}.'.format(n1,n2,resultado))
    elif opcao == 3:
        if n1>n2:
            maior = n1
        else: 
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os valores novamente:')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando ..')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' *10)
print('Fim do programa.')

