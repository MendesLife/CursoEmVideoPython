import moeda

n = float(input('Digite o preço: R$'))
porcento = int(input('Digite a porcentagem que deseja: '))
print(f'A metade de {n} é {moeda.metade(n)}')
print(f'A metade de {n} é {moeda.dobro(n)}')
print(f'Aumentando {porcento}% de {n} é {moeda.aumentar(n, porcento)}')
print(f'Diminuindo {porcento}% de {n} é {moeda.diminuir(n, porcento)}')