valor = float(input('Digite o valor da casa:'))
salario = float(input('Digite o valor do seu salário: '))
anos = float(input('Digite a quantidade de anos que você ira pagar a casa: '))

mensal = valor/(anos*12)
porcentagem = salario*0.3

if mensal > porcentagem:
    print('Você não pode pagar o valor da parcela é muito alto sendo R${:.2f} e 30% do seu salário vale {}.'.format(mensal,porcentagem))
else:
    print('O valor da parcela será de R${}'.format(mensal))