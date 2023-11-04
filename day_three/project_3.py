print('''
 _ __ ___  _   _ ___ _  ___ 
| '_ ` _ \| | | / __| |/ __|
| | | | | | |_| \__ \ | (__ 
|_| |_| |_|\__,_|___/_|\___|''')

print("Bem-vindo a sua jukebox virtual")
print("A sua missão é escolher uma música.")

first = input('Pabllo Vittar ou Urias? - Insira "P" ou "U"')
first_lower = first.lower()

if first_lower == "p": 
    second = input('Você tá triste ou alegre? - Insira "T" ou "A"')
    second_lower = second.lower()
    if second_lower == "t":
        print("Ouça - Triste com T")
    else: 
        print("Ouça - Zap Zum")
elif first_lower == "u":
    three = input('Urias cantando inglês ou português - Insira "I" ou "P"')
    three_lower = three.lower()
    if three_lower == "p":
        print("Ouça - Foi Mal")
    else:
        print("Ouça - Her Mind")

print("Música é o que permite a gente viajar sem sair do lugar.")



