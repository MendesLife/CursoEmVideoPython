import random

velocidade = random.randint(60,90)
limite = 80
multa = (velocidade - limite)*7

if velocidade > 80:
    print('Você foi multado seu otário, porque estava andando a {}km/h sendo que o limite da via é 80km/h, você tera que pagar o valor de R${} de multa.'.format(velocidade,multa))
else:
    print('Taca-lhe pau nesse carrinho, ta muito lento meu filho você está andando a apenas {}km/h vai chegar nunca.'.format(velocidade))