txt = input()
count = 0
l = []
l_reverso = []

if not txt:
    print("vazio\n0")

elif len(txt) != 0:
  for i in txt:
    if (i == "1") or (i == "2") or (i == "3") or (i == "4") or (i == "5") or (i == "6") or (i == "7") or (i == "8") or (i == "9"):
        count += 1
        print("numeros\n0")
        break

if len(txt) != 0 and count == 0:
    txt.replace("a", "@")
    if txt.replace("a", "@") != txt:
        txt = txt.replace("a", "@")
        
    txt.replace("A", "@")
    if txt.replace("A", "@") != txt:
        txt = txt.replace("A", "@")
        
    txt.replace("e", "3")
    if txt.replace("e", "3") != txt:
        txt = txt.replace("e", "3")
        
    txt.replace("E", "3")
    if txt.replace("E", "3") != txt:
        txt = txt.replace("E", "3")
        
    txt.replace("i", "1")
    if txt.replace("i", "1") != txt:
        txt = txt.replace("i", "1")
        
    txt.replace("I", "1")
    if txt.replace("I", "1") != txt:
        txt = txt.replace("I", "1")
        
    txt.replace("o", "0")
    if txt.replace("o", "0") != txt:
        txt = txt.replace("o", "0")
        
    txt.replace("O", "0")
    if txt.replace("O", "0") != txt:
        txt = txt.replace("O", "0")
        
    txt.replace("t", "7")
    if txt.replace("t", "7") != txt:
        txt = txt.replace("t", "7")
        
    txt.replace("T", "7")
    if txt.replace("T", "7") != txt:
        txt = txt.replace("T", "7")
        
    txt.replace("s", "5")
    if txt.replace("s", "5") != txt:
        txt = txt.replace("s", "5")
        
    txt.replace("S", "5")
    if txt.replace("S", "5") != txt:
        txt = txt.replace("S", "5")
        
    txt.replace("S", "5")
    if txt.replace("S", "5") != txt:
        txt = txt.replace("S", "5")
        
    for i in txt:
        l.append(i)
    l_reverso = l[::-1]
    for i in l_reverso:
        if (i == "@") or (i == "3") or (i == "1") or (i == "0") or (i == "7") or (i == "5"):
          count += 1
        print(i, end = "")
    print("")
    print(count)
