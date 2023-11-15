import random
from jogo_forca import lista_palavras
from estagios import stages
from logo  import ascii_art
import os 

print("===================================================")
print(ascii_art)
print("===================================================")

palavra_escolhida = random.choice(lista_palavras).lower()
vidas = 6
display = ["-" for _ in palavra_escolhida]
tentativas = []

def clear():
    os.system('cls')

while "-" in display and vidas > 0:
    palpite = input("ADIVINHE UMA LETRA:").lower()

    clear() 
    tentativas.append(palpite)

    if palpite in palavra_escolhida:
        for indice, letra in enumerate(palavra_escolhida):
            if letra == palpite:
                display[indice] = palpite
                if tentativas.count(palpite) > 1:
                    print(f"Você já falou a letra {palpite}, escolha uma diferente.")
    else:
        vidas -= 1
        print(f"A letra {palpite} não tem na palavra. Você perdeu uma tentiva. Restam somente {vidas} tentativas.")
  
    print(f"{' '.join(display)}")
    print(stages[vidas])

if vidas == 0 and "-" in display:
    print("Você perdeu.:(")
else:
    print("Você ganhou. o/")



