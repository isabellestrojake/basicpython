def reverso_numero(numero):
    return int(str(numero)[::-1])


numero = 127
print("O reverso de", numero, "é:", reverso_numero(numero))
