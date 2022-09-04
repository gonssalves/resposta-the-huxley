a = int(input(" "))
b = int(input(" "))
c = int(input(" "))

if a == 1 and b == 0 and c == 0 or a == 0 and b == 1 and c == 1:
    print("A")
elif b == 1 and a == 0 and c == 0 or b == 0 and a == 1 and c == 1:
    print("B")
elif c == 1 and b == 0 and a == 0 or c == 0 and b == 1 and a == 1:
    print("C")
else:
    print("*\n")
