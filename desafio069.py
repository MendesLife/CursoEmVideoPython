continuar = 'S'
maioridade = 0
homens = 0
mulheresmenores = 0

while continuar == 'S':
    idade = int(input('Digite qual a sua idade: '))
    sexo = str(input('Digite qual o seu sexo: ')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Sexo inválido, digite novamente seu sexo:')).strip().upper()
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if idade > 18:
        maioridade +=1
    if sexo =='M':
        homens +=1
    if idade <20 and sexo == 'F':
        mulheresmenores += 1
    if continuar =='N':
        break

print(f'O número de pessoas maiores de 18 anos é {maioridade}')
print(f'O número de homens cadastrados é {homens}')
print(f'O número de mulheres menores de 20 anos é {mulheresmenores}')