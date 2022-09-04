def Mensagem():
  global ano
  ano = int(input())

def contarDigitos():
  while True:
    Mensagem()
    if ano == -1:
      break
    ehBissexto()
    
def ehBissexto():
    if len(str(ano)) < 4:
      print("Ano invalido")
    elif (ano % 4 == 0 and ano % 100 != 0 and ano == 2152) or (ano % 400 == 0 and ano == 2152):
      print("O ano", ano, "eh bissexto")
    elif (ano % 4 == 0 and ano % 100 != 0 and ano < 2152) or (ano % 400 == 0 and ano < 2152):
      print("O ano", ano, "foi bissexto")
    elif (ano % 4 == 0 and ano % 100 != 0 and ano > 2152) or (ano % 400 == 0 and ano > 2152):
      print("O ano", ano, "serah bissexto")
    else:
      print("O ano", ano, "NAO eh bissexto")




Mensagem()
ehBissexto()
contarDigitos()











