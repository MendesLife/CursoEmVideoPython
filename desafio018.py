import math

an= float(input('Digite o ângulo que você deseja: '))
sen= math.sin(math.radians(an))

print('O ângulo de {} tem o seno de {:.2f} '.format(an,sen))

cosseno = math.cos(math.radians(an))
print('O ângulo de {} tem o cosseno de {:.2f} '.format(an,cosseno))

tangente = math.tan(math.radians(an))
print('O ângulo {} tem a tangente {:.2f}'.format(an,tangente))