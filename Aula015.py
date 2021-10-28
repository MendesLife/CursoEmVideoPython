# while true:
#     if terra:
#         passo
#     if espaço
#         pula
#     if moeda
#         pega
#     if trofeu
#         pega
#         break
# pega

# cont = 1 
# while cont <=10:
#     print(cont,'->', end='')
#     cont +=1
# print('Acabou')

# n= (int(input('Digite um número: ')))
# cont = 1
# soma = n
# while cont != 5:
#     n= (int(input('Digite um número: ')))
#     cont +=1
#     soma = soma + n
# print(soma)

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}.')