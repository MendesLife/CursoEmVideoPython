pessoas = []
dados = []
mai=men=0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1]< men:
            men = dados[1]
    pessoas.append(dados[:]) 
    dados.clear()
    resp = str(input('Deseja continuar [S/N] ? '))
    if resp in 'Nn':
        break

print(f'Os dados foram {pessoas}.')
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O mais pesado foi de {mai}Kg. Peso de', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]',end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ',end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}',end='')
print()