def contar_vogais(frase):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1
    return contador


frase = input("Digite uma frase: ")
print("Total de vogais na frase:", contar_vogais(frase))
