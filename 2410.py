num = int(input())

acumulador = 1
rodadas = 0
continua = True
while continua:
    for i in range(1, 7):
        rodadas += 1
        acumulador += i
        if acumulador == num:
            continua = False
            break
        elif acumulador > num:
            acumulador -= num

print(rodadas)

