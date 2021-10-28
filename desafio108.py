import moeda

n = float(input('Digite o preço: R$'))
porcento = int(input('Digite a porcentagem que deseja: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')

print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')

print(f'Aumentando {porcento}% de {moeda.moeda(n)} é {moeda.moeda(moeda.aumentar(n, porcento))}')

print(f'Diminuindo {porcento}% de {moeda.moeda(n)} é {moeda.moeda(moeda.diminuir(n, porcento))}')