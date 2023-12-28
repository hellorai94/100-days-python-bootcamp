# Cria a função 
def prime_checker(number):
    # Define is_prime como Verdadeiro
    is_prime = True
    # Cria uma interação para ir vendo os números que estão dentro do range
    # Começando de 2, porque é o menor número primo e indo até o limite do número que deve ser checado
    for i in range(2, number):
        # Verifica se algum número traz o resto  0 em uma divisão, se trouxer, seta a variável is_prime como False
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input()) 
prime_checker(number=n)