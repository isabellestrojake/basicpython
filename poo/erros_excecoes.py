def calcular_media(valores):
    tamanho = len(valores)
    soma = sum(valores)
    media = soma / tamanho
    return media


valores = []


while True:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == "ok":
        break
    try:
        valor = float(valor)
        valores.append(valor)
    except ValueError:
        print("Por favor, digite apenas números.")


if valores:
    media = calcular_media(valores)
    print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))
else:
    print("Nenhum valor foi inserido para calcular a média.")
