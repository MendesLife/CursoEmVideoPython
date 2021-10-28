import moeda

n = float(input('Digite o preço: R$'))
porcentoAumenta = int(input('Digite a porcentagem que deseja aumentar: '))
porcentoReduz =int(input('Digite a porcentagem que deseja reduzir: '))
formata = str(input('Deseja formatar os valores [S/N]: ')).strip().upper()

print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n,formata)}')

print(f'A metade de {moeda.moeda(n)} é {moeda.dobro(n,formata)}')

print(f'Aumentando {porcentoAumenta}% de {moeda.moeda(n)} é {moeda.aumentar(n, porcentoAumenta)}')

print(f'Diminuindo {porcentoReduz}% de {moeda.moeda(n)} é {moeda.diminuir(n, porcentoReduz)}')