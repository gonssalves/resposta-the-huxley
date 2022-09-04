texto = input("")
contador = {}


for c in texto:
    contador.setdefault(c, 0)
    contador[c] = contador[c] + 1
    a = sorted(contador.items(), key=lambda x: x[0], reverse=True)

for i in a:
    print(*i, sep = ' ')
