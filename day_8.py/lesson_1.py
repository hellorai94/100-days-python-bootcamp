# Importa a módulo math
import math

# Define a funcao e coloca os parametros
def paint_calc(height, width, cover):
    # Faz a operação de altura * largura e divide por 5, que a quantidade de metros que uma lata de tinta pinta
    # Usa a math.ceil para arredondar o resultado
    paint = math.ceil((height * width) / cover)
    print(f"You'll need {paint} cans of paint.")

test_h = int(input()) 
test_w = int(input()) 
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
