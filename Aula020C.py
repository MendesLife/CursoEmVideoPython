def dobra(list):
    pos = 0
    while pos < len(list):
        list(pos) *=2
        pos+=1


valores =[6,2,3,9,1]
dobra(valores)
print(valores)