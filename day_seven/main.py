import random

lista_palavras = ["banana", "castelo", "tempo"]

palavra_escolhida = random.choice(lista_palavras)

print(palavra_escolhida)

palpite = input("Adivinhe uma letra:").lower()

for letra in palavra_escolhida:
    if letra == palpite:
        print("Acertou")
    else:
        print("Errou")

