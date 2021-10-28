import moeda

n = float(input('Digite o preço: R$'))
porcentagemAumento = int(input('Digite a porcentagem que deseja aumentar: '))
porcentagemReduz = int(input('Digite a porcentagem que deseja reduzir: '))
formata = str(input('Deseja formatar [S/N] ')).upper()


moeda.resumo(n,porcentagemAumento,porcentagemReduz)