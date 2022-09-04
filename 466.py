cidade = input().upper()
l = ["",None,None]

while(cidade != "FIM"):
    km = int(input())
    passagem = float(input())
    passagem *= 2
    if(l[1] is None):
        if(passagem <= 300):
            l[1] = km
            l[2] = passagem
            l[0] = cidade
    elif(passagem <= 300 and l[1] < km):
            l[1] = km
            l[2] = passagem
            l[0] = cidade
    cidade = input().upper()

if(l[0] == ""):
    print("SEM DESTINO")
else:
    print(l[0])

