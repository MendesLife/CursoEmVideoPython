salario = float(input('Digite o seu salário: '))

aumento = 0

if salario > 1250:
    aumento = salario+(salario*10)/100
    print('Seu salário tem o valor de {} com o aumento de 10% ele fica \033[32m{}\033[m.'.format(salario, aumento))
if salario <= 1250:
    aumento = salario+(salario*15)/100
    print('Seu salário tem o valor de {} com o aumento de 15% ele fica \033[32m{}\033[m.'.format(salario, aumento))