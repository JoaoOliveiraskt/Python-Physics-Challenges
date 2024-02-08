'''
1. Calcular a força normal exercida sobre um objeto em um plano inclinado,
 dado o ângulo de inclinação e a massa do objeto.
'''


import math

angulo = float(input("Digite o ângulo de inclinação (em graus): "))
massa = float(input("Digite a massa do objeto (em kg): "))

angulo_rad = math.radians(angulo)

aceleracao_gravitacional = 9.8  

forca_normal = massa * aceleracao_gravitacional * math.cos(angulo_rad)

print(f"A força normal exercida sobre o objeto é: {forca_normal} N")

