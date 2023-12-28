from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, shift_amount, choose_direction):
    # Transformo a string em uma lista
    list_text = list(plain_text)
    cipher_text = ""
    # Pecorro os valores da lista
    for i in list_text:
        # Pego o índice da letra da palavra que deve ser criptograda na lista principal
        index_alphabet = alphabet.index(i)
        if choose_direction == "encode":
        # Crio o novo índice, pegando o atual e acrescentando o valor da variável 'shift'
            new_index = min(index_alphabet + shift_amount, len(alphabet) - 1)
        elif choose_direction == "decode":
            new_index = min(index_alphabet - shift_amount, len(alphabet) - 1)
        # Vou concatendo os valores para formar a palavra criptografada
        cipher_text += alphabet[new_index]

    print(f"The {direction} text is {cipher_text}")

caesar(plain_text=text, shift_amount=shift, choose_direction=direction)




