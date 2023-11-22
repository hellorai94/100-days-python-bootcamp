alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    # Transformo a string em uma lista
    list_text = list(plain_text)
    cipher_text = ""
    # Pecorro os valores da lista
    for i in list_text:
        # Pego o índice da letra da palavra que deve ser criptograda na lista principal
        index_alphabet = alphabet.index(i)
        # Crio o novo índice, pegando o atual e acrescentando o valor da variável 'shift'
        new_index = min(index_alphabet + shift_amount, len(alphabet) - 1)
        # Vou concatendo os valores para formar a palavra criptografada
        cipher_text += alphabet[new_index]

    print(f"The encoded text is {cipher_text}")

def decrypt(plain_text, shift_amount):
    # Transformo a string em uma lista
    list_text = list(plain_text)
    cipher_text = ""
    # Pecorro os valores da lista
    for i in list_text:
        # Pego o índice da letra da palavra que deve ser criptograda na lista principal
        index_alphabet = alphabet.index(i)
        # Crio o novo índice, pegando o atual e acrescentando o valor da variável 'shift'
        new_index = min(index_alphabet - shift_amount, len(alphabet) - 1)
        # Vou concatendo os valores para formar a palavra criptografada
        cipher_text += alphabet[new_index]

    print(f"The decode text is {cipher_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text, shift_amount=shift)




