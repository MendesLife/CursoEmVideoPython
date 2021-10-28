alunos = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunos.append([nome,[nota1,nota2], media])
    resp = str(input('Deseja continuar [S/N]: '))
    if resp in 'Nn':
        break

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(alunos):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(alunos)-1:
        print(f'Notas de {alunos[opc-1][0]} são {alunos[opc-1][1]}')
print('<<< VOlTE Sempre >>>')
