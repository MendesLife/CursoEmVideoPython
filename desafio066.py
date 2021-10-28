n = s = c = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma vale {s} e a quantidade de números utilizados foi {c}.')