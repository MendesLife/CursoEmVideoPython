continuar = 'S'
total = 0
caro = 0


while continuar == 'S':
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if total == 0:
        barato = preco
        nomeBarato = nome
    total = total + preco
    if preco > 1000:
        caro +=1
    if preco < barato:
        barato = preco
        nomeBarato = nome
    if continuar =='N':
        break

print(f'O total gasto é {total}.')
print(f'A quantidade de produtos que custam mais de R$1000,00 são {caro}.')
print(f'O nome do produto mais barato é {nomeBarato}.')
