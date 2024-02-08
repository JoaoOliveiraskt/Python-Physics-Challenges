def calcularDistanciaPercorrida(velocidade1, velocidade2, distanciaTotal):
    area = (1/2) * (velocidade1 + velocidade2) * distanciaTotal
    return area

velocidade1 = float(input("Digite a velocidade 1 em metros: "))
velocidade2 = float(input("Digite a velociade 2 em metros: "))
distanciaTotal = float(input("Digite o deslocamento em metros: "))

distanciaPercorridaPeloCarro = calcularDistanciaPercorrida(velocidade1, velocidade2, distanciaTotal)

print(f"A distância percorrida pelo carro foi de {distanciaPercorridaPeloCarro:.2f} metros.")
