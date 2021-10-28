pn = float(input('Digite o valor do produto: '))
cp = input('Qual é a condição de pagamento: ').strip().upper()

if cp == 'DINHEIRO':
    print('O valor no dinheiro tem 10% de desconto sendo assim o produto fica no valor de {}.'.format(pn-(pn*0.10)))
elif cp == 'CARTAO': 
    print('O valor no cartão a vista tem 5% de desconto sendo assim o produto fica no valor de {}.'.format((pn*0.95)))
elif cp == '2 PARCELAS': 
    print('O valor em duas parcelas é de {} x2, sendo o valor total de {}.'.format(pn/2,pn))
elif cp == '3 PARCELAS': 
    print('O valor em tres parcelas tem um juros de 30% e fica {} x3, sendo o valor total de {}.'.format(((pn*1.20))/3,(pn*1.20)))
