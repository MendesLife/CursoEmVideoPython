c = 0
t = 0

while True:
    n = int(input('Qual número deseja realizar a tabuada: '))
    if n < 0:
        break
    for c in range(0,10):
        c += 1
        t = n*c
        print(t)
    print('=-=' *10)
print('FIM')