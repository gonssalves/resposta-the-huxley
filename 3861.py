x = int(input(""))
if 1 <= x < 12:
  print("Você é uma crian~a.")
elif 12 <= x < 18:~
  print("Você é um adolescente.")
elif 18 <= x < 36:
  print("Você é um jovem.")
elif 36 <= x < 65:
  print("Você é um adulto.")
elif x < 0:
  print("Você ainda não nasceu.")
else:
  print("Voc é um idoso.")
