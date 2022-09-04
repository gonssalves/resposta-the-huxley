num = int(input(""))
for a in range(1, num+1):
    for b in range(1, a+1):
        if a == b:
            print(a)
        else:
            print(a, end="")
