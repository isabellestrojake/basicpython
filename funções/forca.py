import random


palavras = ['python', 'programacao', 'computador', 'algoritmo', 'desenvolvimento']


def escolher_palavra():
    return random.choice(palavras)


def jogar_forca():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 6
    letras_usadas = []

    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while True:
        print("Palavra:", " ".join(palavra_oculta))
        print("Tentativas restantes:", tentativas)
        print("Letras usadas:", ", ".join(letras_usadas))

        if '_' not in palavra_oculta:
            print("Parabéns! Você acertou a palavra:", palavra)
            break

        if tentativas == 0:
            print("Você excedeu o número máximo de tentativas. A palavra era:", palavra)
            break

        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_usadas.append(letra)

        if letra in palavra:
            print("A letra", letra, "está na palavra!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            print("A letra", letra, "não está na palavra.")
            tentativas -= 1


jogar_forca()
