num = input(" ").split()
qnt_comp = int(num[0])
comps = []
for x in range(qnt_comp):
    tempo = input("").split()
    total = 0
    for y in tempo:
        y = int(y)
        total = total + y
    comps.append((total, x+1))
comps.sort()
print(comps[0][1])
