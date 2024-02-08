'''
    3. Calcular a aceleração de um objeto em um plano inclinado, levando
    em consideração a força aplicada, a força de atrito e a força normal.
'''


import math

# Solicitar ao usuário os valores necessários
forca_aplicada = float(input("Digite o valor da força aplicada: "))
forca_atrito = float(input("Digite o valor da força de atrito: "))
forca_normal = float(input("Digite o valor da força normal: "))
angulo_inclinacao = float(input("Digite o ângulo de inclinação do plano: "))

# Converter o ângulo de graus para radianos
angulo_radianos = math.radians(angulo_inclinacao)

# Calcular a aceleração
aceleracao = (forca_aplicada - forca_atrito * math.sin(angulo_radianos)) / (forca_normal + forca_atrito * math.cos(angulo_radianos))

# Exibir o resultado
print(f"A aceleração do objeto é: {aceleracao} m/s²")
