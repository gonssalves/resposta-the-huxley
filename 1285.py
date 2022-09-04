def calcular_nota(resposta, gabarito):
    nota = 0
    for i in range(len(resposta)):
        if resposta[i] == gabarito[i]:
            nota += 1
    return nota

linha = input()
dic_respostas = {}

while linha != "*":
    nome, resposta = linha.split()
    dic_respostas[nome] = resposta
    linha = input()

gabarito = input()

respostas = dic_respostas.values()
notas = []
for resps in respostas:
    notas.append(calcular_nota(resps, gabarito))

media = sum(notas)/len(notas)
maior = max(notas)
menor = min(notas)

print("Maior:", maior)
print("Menor:", menor)
print("Media: %.2f" % media)
