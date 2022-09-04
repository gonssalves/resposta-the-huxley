def remover_especiais(palavra):
    caracteres_especias = '. " ( * $ # :'.split()
    for char_esp in caracteres_especias:
        palavra = palavra.replace(char_esp, " ")
    return palavra

continua = True
lista_frases = []
lista_palavras = []

while continua:
    frase = input().lower()
    if frase == "-1":
        break
    frase = remover_especiais(frase)
    lista_palavras.extend(frase.split())

meu_dicionario = set(lista_palavras)

for palavra in sorted(meu_dicionario):
    qtd = lista_palavras.count(palavra)
    print(palavra, qtd)


